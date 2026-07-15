import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "airbnb.db"
)

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()

print("\nTables in Database:\n")

for table in tables:
    print(table[0])

conn.close()