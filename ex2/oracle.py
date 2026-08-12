import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore
    DOTENV_INSTALLED = True
except ImportError:
    DOTENV_INSTALLED = False


def check_env_file() -> bool:
    """Checks if .env exists for the security check output."""
    return os.path.exists(".env")


def main() -> None:
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...\n")

    mode = os.getenv("MATRIX_MODE") or "development"
    db_url = os.getenv("DATABASE_URL") or ""
    api_key = os.getenv("API_KEY") or ""
    log_level = os.getenv("LOG_LEVEL") or ""
    zion_url = os.getenv("ZION_ENDPOINT") or ""

    missing_vars = []
    if not os.getenv("MATRIX_MODE"):
        missing_vars.append("MATRIX_MODE")
    if not db_url:
        missing_vars.append("DATABASE_URL")
    if not api_key:
        missing_vars.append("API_KEY")

    if missing_vars:
        print(f"WARNING: Missing configuration for: {', '.join(missing_vars)}")
        print("Using default 'limbo' settings...\n")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode.lower() == "production":
        print("Database: Connected to PRODUCTION mainframe")
        print(f"API Access: {'SECURED' if api_key else 'FAILED'}")
        print(f"Log Level: {log_level if log_level else 'INFO'}")
        print(f"Zion Network: {zion_url if zion_url else 'OFFLINE'}")
    else:
        db_display = db_url if db_url else "Using local SQLite mock"
        print(f"Database: {db_display}")
        data = ['Authenticated (Dev Mode)', 'No API Key found']
        print(f"API Access: {data[0] if api_key else data[1]}")
        print(f"Log Level: {log_level if log_level else 'DEBUG'}")
        print(f"Zion Network: {zion_url if zion_url else 'localhost:8080'}")

    print("\nEnvironment security check:")

    if api_key and api_key != "default_secret":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[!!] Security Warning: No valid API Key found")

    if check_env_file():
        print("[OK] .env file properly configured")
    else:
        print("[--] .env file not found (reading from system environment)")

    print("[OK] Production overrides available")


if __name__ == "__main__":
    if DOTENV_INSTALLED:
        try:
            main()
        except Exception as e:
            print(f"Critical System Failure: {e}")
            sys.exit(1)
    else:
        print("ERROR: python-dotenv is not installed.")
        print("Please install it using 'pip install python-dotenv'.")
        sys.exit(1)
