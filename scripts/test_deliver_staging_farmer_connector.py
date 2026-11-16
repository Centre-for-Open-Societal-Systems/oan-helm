"""scripts/ci/deliver_staging_farmer_connector.sh with a stand-in helm (no cluster): extra arguments reach the
connector upgrade only, after the staging values, so the Farmer pipeline's image override wins over the pin."""
import os
import shutil
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = "scripts/ci/deliver_staging_farmer_connector.sh"
HELM = '#!/usr/bin/env bash\nprintf "%s\\n" "$*" >> "$HELM_LOG"\n'


@unittest.skipUnless(shutil.which("bash"), "needs bash")
class FarmerConnectorDeliveryTest(unittest.TestCase):
    def run_script(self, *args):
        with tempfile.TemporaryDirectory() as tmp:
            bin_dir = Path(tmp) / "bin"
            bin_dir.mkdir()
            helm = bin_dir / "helm"
            helm.write_text(HELM, newline="\n")
            helm.chmod(helm.stat().st_mode | stat.S_IXUSR)
            log = Path(tmp) / "helm.log"
            env = dict(os.environ, PATH=str(bin_dir) + os.pathsep + os.environ["PATH"], HELM_LOG=str(log))
            done = subprocess.run(["bash", SCRIPT, *args], cwd=str(ROOT), env=env, capture_output=True, text=True)
            self.assertEqual(done.returncode, 0, done.stderr)
            return log.read_text().splitlines()

    def test_without_arguments_the_pinned_values_alone_are_used(self):
        credentials, connector = self.run_script()
        self.assertIn("farmer-connector-credentials", credentials)
        self.assertIn("--values environments/staging/values/farmer-connector.yaml --reset-values", connector)

    def test_an_override_reaches_the_connector_upgrade_after_the_staging_values(self):
        credentials, connector = self.run_script("--values", "/tmp/override.json")
        self.assertNotIn("override", credentials)
        self.assertIn("--values environments/staging/values/farmer-connector.yaml --values /tmp/override.json "
                      "--reset-values --atomic", connector)


if __name__ == "__main__":
    unittest.main()
