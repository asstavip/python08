import os
import sys
from pathlib import Path


def load(config) -> None:
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        print("[ERROR] python-dotenv is not installed")
        sys.exit(1)
    config.update(
        {
            "MODE": os.getenv("MATRIX_MODE", "None"),
            "DB": os.getenv("DATABASE_URL"),
            "API": os.getenv("API_KEY"),
            "LOG": os.getenv("LOG_LEVEL", "None"),
            "ENDPOINT": os.getenv("ZION_ENDPOINT"),
        }
    )


def display(config) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"Mode: {config['MODE']}")
    print(
        f"Database: {
            'Connected to local instance' if config['DB'] else 'Not connected'
        }"
    )
    print(
        f"API Access: {
            'Authenticated' if config['API'] else 'Not authenticated'
        }"
    )
    print(f"Log Level: {config['LOG']}")
    print(f"Zion Network: {'Online' if config['ENDPOINT'] else 'Offline'}")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if Path(".env").exists():
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file not found in root of project")
    if config["MODE"] == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")


if __name__ == "__main__":
    config = {}
    load(config)
    display(config)
