"""Publish a validated, 0600 snapshot of ONE Kubernetes Secret generation.

Embedded verbatim by the chart (``python -I -c <this file>``) as the init container of
the worker and receipt-ingress pods. Standard library only.

Why: Kubernetes projects a Secret volume as

    <source>/..data -> ..<timestamp>     symlink, switched atomically on update
    <source>/..<timestamp>/<key>          the files of one generation
    <source>/<key> -> ..data/<key>

Opening ``<source>/tls.crt`` and then ``<source>/tls.key`` can cross a generation switch
and return an old certificate with a new key. This script resolves ``..data`` once, reads
every file through that generation directory, confirms ``..data`` still points to it,
validates the set (the key matches the certificate; the CA, if any, parses), and only then
publishes it. A changed or vanished generation retries the WHOLE set; after the last
attempt it exits non-zero and publishes nothing. It never publishes a mixed or invalid set.

Published layout in ``<dest>`` (a memory emptyDir):

    <dest>/.gen-<id>/<files>     files 0600, directory 0700, owned by the running uid
    <dest>/current -> .gen-<id>  replaced atomically (os.replace of a symlink)

Readers use ``<dest>/current/<file>``. A crash at any point leaves either the previous
complete set or none; leftovers are removed by the next successful run, so a rerun (pod
restart) is safe.
"""

from __future__ import annotations

import argparse
import os
import secrets
import shutil
import ssl
import sys
import time
from collections.abc import Callable

DATA_LINK = "..data"
CURRENT = "current"


class SnapshotError(Exception):
    """The snapshot could not be published. Messages never contain file contents."""


class GenerationChanged(SnapshotError):
    """``..data`` switched (or the generation vanished) while the set was being read."""


def _read_bytes(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def resolve_generation(source: str) -> str:
    try:
        target = os.readlink(os.path.join(source, DATA_LINK))
    except OSError:
        raise SnapshotError(
            f"{source}/{DATA_LINK} is missing: not a Kubernetes Secret volume; refusing "
            "to read files without a pinned generation") from None
    if os.path.isabs(target) or os.sep in target or not target.startswith(".."):
        raise SnapshotError(f"unexpected {DATA_LINK} target")
    return target


def read_generation(source: str, names: list[str],
                    read: Callable[[str], bytes] = _read_bytes) -> tuple[str, dict[str, bytes]]:
    gen = resolve_generation(source)
    data: dict[str, bytes] = {}
    try:
        for name in names:
            data[name] = read(os.path.join(source, gen, name))
    except FileNotFoundError:
        raise GenerationChanged("generation vanished during read") from None
    if resolve_generation(source) != gen:
        raise GenerationChanged("generation switched during read")
    return gen, data


def _write_0600(path: str, content: bytes) -> None:
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(fd, content)
    finally:
        os.close(fd)
    os.chmod(path, 0o600)


def _validate(gen_dir: str, cert: str, key: str, ca: str | None) -> None:
    key_path = os.path.join(gen_dir, key)
    if os.stat(key_path).st_mode & 0o077:
        raise SnapshotError("staged key is accessible by group or others")
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    try:
        ctx.load_cert_chain(certfile=os.path.join(gen_dir, cert), keyfile=key_path)
    except (ssl.SSLError, OSError, ValueError):
        raise SnapshotError("certificate and key do not form a valid pair") from None
    if ca is not None:
        try:
            ctx.load_verify_locations(cafile=os.path.join(gen_dir, ca))
        except (ssl.SSLError, OSError, ValueError):
            raise SnapshotError("CA bundle could not be loaded") from None


def _cleanup(dest: str, keep: str | None) -> None:
    for entry in os.listdir(dest):
        path = os.path.join(dest, entry)
        if entry.startswith(".gen-") and entry != keep:
            shutil.rmtree(path, ignore_errors=True)
        elif entry.startswith(".current.tmp-"):
            try:
                os.unlink(path)
            except FileNotFoundError:
                pass


def publish_once(source: str, dest: str, cert: str, key: str, ca: str | None,
                 read: Callable[[str], bytes] = _read_bytes) -> str:
    names = [cert, key] + ([ca] if ca else [])
    _gen, data = read_generation(source, names, read)
    gen_name = ".gen-" + secrets.token_hex(8)
    gen_dir = os.path.join(dest, gen_name)
    os.mkdir(gen_dir, 0o700)
    os.chmod(gen_dir, 0o700)
    try:
        for name, content in data.items():
            _write_0600(os.path.join(gen_dir, name), content)
        _validate(gen_dir, cert, key, ca)
        tmp = os.path.join(dest, ".current.tmp-" + secrets.token_hex(8))
        os.symlink(gen_name, tmp)
        os.replace(tmp, os.path.join(dest, CURRENT))  # atomic switch to the new set
    except BaseException:
        shutil.rmtree(gen_dir, ignore_errors=True)
        raise
    _cleanup(dest, keep=gen_name)
    return gen_name


def snapshot(source: str, dest: str, cert: str, key: str, ca: str | None = None, *,
             attempts: int = 5, delay: float = 1.0,
             read: Callable[[str], bytes] = _read_bytes,
             sleep: Callable[[float], None] = time.sleep) -> str:
    """Publish one validated generation, retrying the whole set; raise if impossible."""
    if attempts < 1:
        raise ValueError("attempts must be >= 1")
    last: SnapshotError | None = None
    for attempt in range(1, attempts + 1):
        try:
            return publish_once(source, dest, cert, key, ca, read)
        except SnapshotError as exc:
            last = exc
            if attempt < attempts:
                sleep(delay)
    raise SnapshotError(f"no consistent, valid set after {attempts} attempts: {last}")


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="tls_snapshot")
    p.add_argument("--source", required=True)
    p.add_argument("--dest", required=True)
    p.add_argument("--cert", required=True)
    p.add_argument("--key", required=True)
    p.add_argument("--ca")
    p.add_argument("--attempts", type=int, default=5)
    p.add_argument("--delay", type=float, default=1.0)
    args = p.parse_args(argv)
    try:
        gen = snapshot(args.source, args.dest, args.cert, args.key, args.ca,
                       attempts=args.attempts, delay=args.delay)
    except SnapshotError as exc:
        print(f"tls_snapshot: {exc}", file=sys.stderr)
        return 1
    print(f"tls_snapshot: published {gen}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
