"""Generate throwaway local-trial certificates into /certs (a Docker volume).

CA -> fake-8028 server cert, OAN 8028 client cert, OAN receipts server cert,
8028 callback client cert (pinned by the receipts ingress). Keys are 0600 and owned by
uid 10001 (the OAN image user). Never use these anywhere but the local trial.
"""

from __future__ import annotations

import datetime as dt
import ipaddress
import os
import sys
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/certs")
UID = 10001
# Service names the certificates are issued for (the release names its Services).
RECEIPTS_HOST = os.environ.get("RECEIPTS_HOST", "oan-receipts")
FAKE8028_HOST = os.environ.get("FAKE8028_HOST", "fake-8028")


def key() -> rsa.RSAPrivateKey:
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def write(name: str, cert: x509.Certificate, k: rsa.RSAPrivateKey | None) -> None:
    (OUT / f"{name}.crt").write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    os.chmod(OUT / f"{name}.crt", 0o644)
    os.chown(OUT / f"{name}.crt", UID, UID)
    if k is not None:
        p = OUT / f"{name}.key"
        p.write_bytes(
            k.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption(),
            )
        )
        os.chmod(p, 0o600)
        os.chown(p, UID, UID)


def issue(
    cn: str,
    issuer: x509.Certificate | None,
    issuer_key: rsa.RSAPrivateKey | None,
    *,
    ca: bool = False,
    dns: list[str] | None = None,
    ips: list[str] | None = None,
    usage: list[x509.ObjectIdentifier] | None = None,
) -> tuple[x509.Certificate, rsa.RSAPrivateKey]:
    k = key()
    now = dt.datetime.now(dt.UTC)
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, cn)])
    b = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(issuer.subject if issuer else name)
        .public_key(k.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - dt.timedelta(minutes=5))
        .not_valid_after(now + dt.timedelta(days=7))
        .add_extension(x509.BasicConstraints(ca=ca, path_length=None), critical=True)
        # Python >= 3.13 verifies strictly (VERIFY_X509_STRICT): key identifiers and,
        # for the CA, key usage are required. Frappe v16 runs Python 3.14.
        .add_extension(x509.SubjectKeyIdentifier.from_public_key(k.public_key()), critical=False)
        .add_extension(
            x509.AuthorityKeyIdentifier.from_issuer_public_key((issuer_key or k).public_key()),
            critical=False,
        )
    )
    if ca:
        b = b.add_extension(
            x509.KeyUsage(
                digital_signature=True,
                content_commitment=False,
                key_encipherment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=True,
                crl_sign=True,
                encipher_only=False,
                decipher_only=False,
            ),
            critical=True,
        )
    if dns or ips:
        names = [x509.DNSName(d) for d in dns or []]
        names += [x509.IPAddress(ipaddress.ip_address(i)) for i in ips or []]
        b = b.add_extension(x509.SubjectAlternativeName(names), critical=False)
    if usage:
        b = b.add_extension(x509.ExtendedKeyUsage(usage), critical=False)
    return b.sign(issuer_key or k, hashes.SHA256()), k


OUT.mkdir(parents=True, exist_ok=True)
if (OUT / "ca.crt").exists():
    print("certificates already present")
    raise SystemExit(0)
ca, ca_key = issue("oan-trial-ca", None, None, ca=True)
write("ca", ca, None)
srv = ExtendedKeyUsageOID.SERVER_AUTH
cli = ExtendedKeyUsageOID.CLIENT_AUTH
write(
    "fake8028-server", *issue(FAKE8028_HOST, ca, ca_key, dns=[FAKE8028_HOST, "localhost"], usage=[srv])
)
write("oan-8028-client", *issue("oan-worker", ca, ca_key, usage=[cli]))
write("receipts-server", *issue(RECEIPTS_HOST, ca, ca_key, dns=[RECEIPTS_HOST], usage=[srv]))
write("callback-client", *issue("8028-callback", ca, ca_key, usage=[cli]))
write(
    "oan-api-server",
    *issue("oan-api", ca, ca_key, dns=["oan-api", "localhost"], ips=["127.0.0.1"], usage=[srv]),
)
print("certificates written")
