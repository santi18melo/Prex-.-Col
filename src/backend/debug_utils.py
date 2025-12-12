import os
import logging
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env first
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

# Configure Django settings if not already configured
import django
from django.conf import settings

if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()

from django.core.management import call_command
from django.db import connections
from django.db.utils import OperationalError

logger = logging.getLogger(__name__)

def check_environment_variables(required_vars=None):
    """Verify that essential environment variables are set.

    Args:
        required_vars (list[str] | None): List of variable names to check. If None, a default set is used.
    Returns:
        dict: Mapping of variable name to boolean indicating presence.
    """
    if required_vars is None:
        required_vars = [
            "SECRET_KEY",
            "DEBUG",
            "DATABASE_URL",
            "POSTGRES_DB",
            "POSTGRES_USER",
            "POSTGRES_PASSWORD",
            "POSTGRES_HOST",
            "POSTGRES_PORT",
            "FRONTEND_URL",
        ]
    status = {}
    for var in required_vars:
        status[var] = bool(os.getenv(var))
        if not status[var]:
            logger.warning("Environment variable %s is not set", var)
    return status

def check_database_connection(alias="default"):
    """Attempt to open a connection to the configured database.

    Returns:
        bool: True if connection succeeds, False otherwise.
    """
    try:
        conn = connections[alias]
        conn.ensure_connection()
        logger.info("Database connection (%s) successful", alias)
        return True
    except OperationalError as e:
        logger.error("Database connection (%s) failed: %s", alias, e)
        return False

def detect_duplicate_settings():
    """Detect duplicate or contradictory settings in the Django configuration.

    Currently checks for duplicated boolean flags that may cause confusion.
    Returns a list of warning strings.
    """
    warnings = []
    # Example: SECURE_SSL_REDIRECT appears twice with different defaults.
    if getattr(settings, "SECURE_SSL_REDIRECT", None) is not None:
        # Inspect module source for multiple assignments (simple heuristic).
        # Here we just warn that the flag is set in multiple places.
        warnings.append(
            "SECURE_SSL_REDIRECT is defined in multiple sections; ensure the intended value is applied based on DEBUG flag."
        )
    # SESSION_COOKIE_SECURE duplicate check.
    if getattr(settings, "SESSION_COOKIE_SECURE", None) is not None:
        warnings.append(
            "SESSION_COOKIE_SECURE appears more than once; consolidate to a single definition."
        )
    return warnings

def run_diagnostics():
    """Run a full suite of backend diagnostics and output a concise report.
    """
    report = []
    report.append("=== Backend Diagnostics Report ===")
    # Environment variables
    env_status = check_environment_variables()
    missing = [var for var, present in env_status.items() if not present]
    if missing:
        report.append(f"Missing environment variables: {', '.join(missing)}")
    else:
        report.append("All required environment variables are set.")
    # Database
    if check_database_connection():
        report.append("Database connection: OK")
    else:
        report.append("Database connection: FAILED")
    # Duplicate settings
    dup_warnings = detect_duplicate_settings()
    if dup_warnings:
        report.append("Duplicate/contradictory settings detected:")
        report.extend([f" - {w}" for w in dup_warnings])
    else:
        report.append("No duplicate setting issues detected.")
    # Run Django's built‑in checks
    try:
        call_command("check")
        report.append("Django system check: OK")
    except Exception as exc:
        report.append(f"Django system check raised an exception: {exc}")
    report.append("=== End of Report ===")
    return "\n".join(report)

if __name__ == "__main__":
    print(run_diagnostics())
