"""Chart seals remain stable after Python test imports on another interpreter."""
import importlib.util
import unittest
import uuid
from pathlib import Path

spec = importlib.util.spec_from_file_location("chart_validation", Path(__file__).with_name("validate.py"))
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


class ChartFingerprintTests(unittest.TestCase):
    def test_runtime_bytecode_is_not_source_but_python_changes_are(self):
        root = validation.ROOT / ".build" / ("fingerprint-test-" + uuid.uuid4().hex)
        root.mkdir(parents=True)
        source = root / "register.py"
        cache = root / "__pycache__"
        cache.mkdir()
        bytecode = cache / "register.cpython-312.pyc"
        legacy_bytecode = root / "register.pyc"
        try:
            source.write_text("print('version one')\n", encoding="utf-8")
            before = validation.fingerprint(root)
            bytecode.write_bytes(b"interpreter-specific cache")
            legacy_bytecode.write_bytes(b"legacy bytecode")
            self.assertEqual(before, validation.fingerprint(root))
            source.write_text("print('version two')\n", encoding="utf-8")
            self.assertNotEqual(before, validation.fingerprint(root))
        finally:
            for file in (source, bytecode, legacy_bytecode):
                file.unlink(missing_ok=True)
            cache.rmdir()
            root.rmdir()


if __name__ == "__main__":
    unittest.main()
