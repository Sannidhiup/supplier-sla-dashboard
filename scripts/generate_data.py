import os
import sqlite3
import random
from datetime import datetime, timedelta
import pandas as pd

# ---------- DATABASE PATH ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "supplier_data.db")

conn = sqlite3.connect(DB_PATH)

# ---------- SUPPLIERS ----------
suppliers = [
    (1, "Tata Steel"),
    (2, "Reliance Logistics"),
    (3, "Jindal Suppliers"),
    (4, "Hindalco"),
    (5, "L&T Components")
    
]

pd.DataFrame(
    suppliers,
    columns=["supplier_id", "supplier_name"]
).to_sql("suppliers", conn, if_exists="replace", index=False)

# ---------- DELIVERIES ----------
delivery_data = []

for i in range(1, 501):
    supplier_id = random.randint(1, 5)
    expected = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
    delivered = expected + timedelta(days=random.randint(-3, 5))
    invoice_amt = random.randint(10000, 90000)
    correct = random.choice([1, 1, 1, 0])
    rejected = 0 if correct == 1 else 1

    delivery_data.append([
        i,
        supplier_id,
        delivered,
        expected,
        invoice_amt,
        correct,
        rejected
    ])

pd.DataFrame(
    delivery_data,
    columns=[
        "delivery_id",
        "supplier_id",
        "delivery_date",
        "expected_date",
        "invoice_amount",
        "invoice_correct",
        "is_rejected"
    ]
).to_sql("deliveries", conn, if_exists="replace", index=False)

# ---------- PAYMENTS ----------
payment_data = []

for i in range(1, 401):
    supplier_id = random.randint(1, 5)
    due = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
    paid = due + timedelta(days=random.randint(0, 20))
    outstanding = random.randint(5000, 60000)

    payment_data.append([
        i,
        supplier_id,
        due,
        paid,
        outstanding
    ])

pd.DataFrame(
    payment_data,
    columns=[
        "payment_id",
        "supplier_id",
        "due_date",
        "paid_date",
        "outstanding_amount"
    ]
).to_sql("payments", conn, if_exists="replace", index=False)

conn.close()

print("Synthetic data generated successfully")
