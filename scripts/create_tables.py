import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "supplier_data.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name TEXT
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS deliveries (
    delivery_id INTEGER PRIMARY KEY,
    supplier_id INTEGER,
    delivery_date DATE,
    expected_date DATE,
    invoice_amount REAL,
    invoice_correct INTEGER,
    is_rejected INTEGER
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY,
    supplier_id INTEGER,
    due_date DATE,
    paid_date DATE,
    outstanding_amount REAL
);
""")

conn.commit()
conn.close()

print("Database and tables created successfully")
