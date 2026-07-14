import sqlite3
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Database folder
DB_FOLDER = BASE_DIR / "Database"
DB_FOLDER.mkdir(exist_ok=True)

# Database file
DB_PATH = DB_FOLDER / "procureai.db"


def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_name TEXT NOT NULL,
        contact_person TEXT,
        phone TEXT,
        email TEXT,
        gst TEXT,
        pan TEXT,
        address TEXT,
        payment_terms TEXT,
        category TEXT,
        currency TEXT,
        bank_details TEXT
    )
    """)

    conn.commit()
    conn.close()

    print(f"Database created at: {DB_PATH}")