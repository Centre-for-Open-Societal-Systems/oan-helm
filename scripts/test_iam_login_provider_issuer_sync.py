"""The pre-upgrade issuer sync leaves the IAM's issuer-keyed seed nothing to insert.

The IAM APIs seed login_providers from the login_providers.json the openg2p-iam-service subchart renders,
inserting every row whose issuer is not in the table, with the id from the file (data_loader
seed_login_providers_by_issuer). These tests render the commons-services chart (helm required, HELM may
name the binary), apply the Job's update to a table that still carries the previous issuer, and run the
seed's own selection over the result: it must select nothing, for every environment's values.
"""
import json
import os
import shutil
import subprocess
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CHART = ROOT / "charts/openg2p-commons-services"
TEMPLATE = CHART / "templates/iam-login-provider-issuer-sync.yaml"
HELM = os.environ.get("HELM") or shutil.which("helm")
SECRETS = ("charts/openg2p-iam-service/templates/iam-staff-portal-api/login-providers-secret.yaml",
           "charts/openg2p-iam-service/templates/iam-agent-portal-api/login-providers-secret.yaml")
UPDATED = ("issuer", "authorization_endpoint", "token_endpoint", "userinfo_endpoint", "server_metadata_url",
           "jwks_uri", "oauth_callback_url")


def render(environment, *only):
    command = [HELM, "template", "commons-services", str(CHART), "-n", "commons",
               "-f", str(ROOT / f"environments/{environment}/values/commons-services.yaml")]
    for path in only:
        command += ["--show-only", path]
    result = subprocess.run(command, capture_output=True, text=True, timeout=300)
    if result.returncode:
        raise AssertionError(result.stderr)
    return [d for d in yaml.safe_load_all(result.stdout) if d]


def job_rows(environment):
    (job,) = render(environment, "templates/iam-login-provider-issuer-sync.yaml")
    (container,) = job["spec"]["template"]["spec"]["containers"]
    return job, json.loads({e["name"]: e for e in container["env"]}["PROVIDER_ROWS"]["value"])


def seeded_rows(environment):
    rows = []
    for secret in render(environment, *SECRETS):
        rows += json.loads(secret["stringData"]["login_providers.json"])
    return rows


def seed_selection(table, rows):
    """iam_staff_portal_api.data.data_loader.seed_login_providers_by_issuer: rows whose issuer is new."""
    existing = {row["issuer"] for row in table}
    return [row for row in rows if row.get("issuer") not in existing]


def apply_job(table, rows):
    """The Job's UPDATE ... FROM jsonb_to_recordset(rows) WHERE lp.id = r.id; never inserts or deletes."""
    by_id = {row["id"]: row for row in rows}
    result = []
    for current in table:
        update = by_id.get(current["id"])
        current = dict(current)
        if update:
            current.update({k: update[k] for k in UPDATED})
            if update["default_redirect_uri"]:
                current["default_redirect_uri"] = update["default_redirect_uri"]
        result.append(current)
    return result


def previous_table(rows, old="https://keycloak.oanstaging.com"):
    """The table as staging has it before the move: every seeded row on the previous Keycloak address, plus
    unrelated rows (the old registry-specific copies of the staff provider) that the Job must not touch."""
    table = []
    for row in rows:
        realm = row["issuer"].split("/realms/", 1)[1]
        previous = dict(row, **{k: f"{old}/realms/{realm}/{k}" for k in UPDATED})
        previous["issuer"] = f"{old}/realms/{realm}"
        table.append(previous)
    staff_copy = {k: f"{old}/realms/staff/{k}" for k in UPDATED}
    staff_copy.update(id=2, issuer=f"{old}/realms/staff", default_redirect_uri="https://farmer-registry.oanstaging.com")
    table.append(staff_copy)
    return table


@unittest.skipUnless(HELM, "helm required")
class IssuerSyncRenderTests(unittest.TestCase):
    def test_job_rows_carry_the_seeded_issuer_and_endpoints_for_every_id(self):
        for environment in ("dev", "staging"):
            with self.subTest(environment=environment):
                _, rows = job_rows(environment)
                seeded = {row["id"]: row for row in seeded_rows(environment)}
                self.assertEqual(sorted(seeded), sorted(row["id"] for row in rows))
                self.assertEqual(sorted(seeded), [1, 10])
                for row in rows:
                    for field in UPDATED:
                        self.assertEqual(row[field], seeded[row["id"]][field], (row["id"], field))

    def test_after_the_job_the_seed_inserts_nothing_when_the_issuer_moves(self):
        for environment in ("dev", "staging"):
            with self.subTest(environment=environment):
                _, rows = job_rows(environment)
                seeded = seeded_rows(environment)
                table = previous_table(seeded)
                # Without the Job the move is exactly the failure: ids 1 and 10 would be inserted again.
                self.assertEqual(sorted(r["id"] for r in seed_selection(table, seeded)), [1, 10])
                after = apply_job(table, rows)
                self.assertEqual(seed_selection(after, seeded), [])
                self.assertEqual(sorted(r["id"] for r in after), sorted(r["id"] for r in table))
                untouched = next(r for r in after if r["id"] == 2)
                self.assertEqual(untouched, next(r for r in table if r["id"] == 2))

    def test_staging_moves_to_the_qa_issuer(self):
        _, rows = job_rows("staging")
        self.assertEqual({r["id"]: r["issuer"] for r in rows},
                         {1: "https://keycloak.qa.oanstaging.com/realms/staff",
                          10: "https://keycloak.qa.oanstaging.com/realms/agent"})
        self.assertEqual(next(r for r in rows if r["id"] == 1)["oauth_callback_url"],
                         "https://staff-iam.qa.oanstaging.com/auth/callback")

    def test_job_runs_before_the_upgrade_only_and_reads_the_password_from_the_iam_secret(self):
        job, _ = job_rows("staging")
        self.assertEqual(job["metadata"]["annotations"]["helm.sh/hook"], "pre-upgrade")
        (container,) = job["spec"]["template"]["spec"]["containers"]
        env = {e["name"]: e for e in container["env"]}
        self.assertEqual(env["PGPASSWORD"], {"name": "PGPASSWORD",
                                             "valueFrom": {"secretKeyRef": {"name": "iam", "key": "iam-db-user"}}})
        self.assertNotIn("value", env["PGPASSWORD"])


class IssuerSyncSqlTests(unittest.TestCase):
    def test_sql_updates_by_id_only_and_never_inserts_or_deletes(self):
        text = TEMPLATE.read_text()
        sql = text[text.index("UPDATE login_providers"):text.index("RETURNING")]
        self.assertIn("WHERE lp.id = r.id", sql)
        for statement in ("INSERT", "DELETE", "TRUNCATE"):
            self.assertNotIn(statement, sql.upper().replace("IS DISTINCT", ""))
        for field in UPDATED:
            self.assertIn(f"{field} = r.{field}", sql)

    def test_selection_mirror_matches_the_iam_rule(self):
        table = [{"id": 1, "issuer": "a"}]
        self.assertEqual(seed_selection(table, [{"id": 1, "issuer": "a"}, {"id": 10, "issuer": "b"}]), [{"id": 10, "issuer": "b"}])


if __name__ == "__main__":
    unittest.main()
