"""ci/jenkins/apply-job.sh must address a job inside its Jenkins folder: at the top level it would create a second
delivery job beside the real one."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
FOLDER = 'https://jenkins.test/job/Helm-and-Data'
# curl stand-in: records every URL; the job's config.xml answers with $JOB_CODE.
CURL = r'''#!/usr/bin/env bash
for a in "$@"; do case "$a" in https://*) url=$a ;; esac; done
echo "$url" >> "$CALLS"
case "$*" in
  *http_code*) printf '%s' "$JOB_CODE" ;;
  *crumbIssuer*) echo '{"crumbRequestField":"Jenkins-Crumb","crumb":"x"}' ;;
esac
'''


class ApplyJob(unittest.TestCase):
    def calls(self, job_code):
        with tempfile.TemporaryDirectory() as tmp:
            for name, body in (('curl', CURL), ('python3', '#!/usr/bin/env bash\ncat >/dev/null\necho Jenkins-Crumb:x\n')):
                path = Path(tmp, name)
                path.write_text(body, encoding='utf-8', newline='\n')
                path.chmod(0o755)
            log = Path(tmp, 'calls')
            env = dict(os.environ, PATH=tmp + os.pathsep + os.environ['PATH'], CALLS=log.as_posix(), JOB_CODE=job_code,
                       JENKINS_URL='https://jenkins.test', JENKINS_USER='u', JENKINS_TOKEN='t')
            subprocess.run([shutil.which('bash'), 'ci/jenkins/apply-job.sh', 'oan-helm-dev-commons'],
                           cwd=ROOT, env=env, check=True, capture_output=True, text=True)
            return log.read_text(encoding='utf-8').split()

    def test_updates_the_job_inside_the_folder(self):
        calls = self.calls('200')
        self.assertEqual(calls[-1], FOLDER + '/job/oan-helm-dev-commons/config.xml')
        self.assertEqual([u for u in calls if u.startswith('https://jenkins.test/job/oan-helm')], [])

    def test_creates_a_missing_job_inside_the_folder(self):
        self.assertEqual(self.calls('404')[-1], FOLDER + '/createItem?name=oan-helm-dev-commons')

    def test_stops_on_any_other_answer_instead_of_creating(self):
        with self.assertRaises(subprocess.CalledProcessError):
            self.calls('403')


if __name__ == '__main__':
    unittest.main()
