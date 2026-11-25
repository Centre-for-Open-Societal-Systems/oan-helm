-- OAN Messaging: least-privilege runtime role (MSG-08, review finding F-09).
--
-- One runtime role for the pilot, used by the API, worker, receipt ingress, cleanup and
-- the operator commands (suspend, resume, status). Migrations run as a separate OWNER
-- role. Per-component roles are deferred (remediation plan §2.4).
--
-- Run as the migration owner (or a superuser) AFTER `alembic upgrade head`, with psql:
--
--   psql "$OWNER_URL" -v ON_ERROR_STOP=1 \
--        -v runtime_role=oan_msg_runtime -v owner_role=oan_msg_owner \
--        -f deploy/sql/grants.sql
--
-- The runtime role must already exist with LOGIN and a password set out of band; this
-- script never creates credentials. It is idempotent and safe to re-run after upgrades.
--
-- What the runtime role can do: read and write rows of the application tables, use their
-- sequences, and take advisory locks (no grant needed). It cannot create, alter or drop
-- objects, truncate tables, or touch the Alembic version table.

REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM :"runtime_role";
GRANT USAGE ON SCHEMA public TO :"runtime_role";

REVOKE ALL ON ALL TABLES IN SCHEMA public FROM :"runtime_role";
GRANT SELECT, INSERT, UPDATE, DELETE ON
    callers,
    api_credentials,
    messages,
    message_content,
    message_attempts,
    receipts,
    retired_key_versions,
    dispatch_controls,
    stats_daily,
    stats_failures,
    stats_campaigns,
    stats_state
TO :"runtime_role";
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO :"runtime_role";

-- Tables added by future migrations are NOT granted automatically: each migration that
-- adds a table must be accompanied by an update to the list above, reviewed with it.
ALTER DEFAULT PRIVILEGES FOR ROLE :"owner_role" IN SCHEMA public
    REVOKE ALL ON TABLES FROM :"runtime_role";
ALTER DEFAULT PRIVILEGES FOR ROLE :"owner_role" IN SCHEMA public
    GRANT USAGE, SELECT ON SEQUENCES TO :"runtime_role";
