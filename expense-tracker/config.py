from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = "dev-secret-key"
    DATABASE_PATH = BASE_DIR / "instance" / "expense_tracker.db"
