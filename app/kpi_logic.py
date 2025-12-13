import sqlite3
import pandas as pd
import os

# -------------------------
# Database Path (ABSOLUTE)
# -------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "supplier_data.db")


# -------------------------
# Load data from database
# -------------------------
def load_data():
    conn = sqlite3.connect(DB_PATH)

    suppliers = pd.read_sql("SELECT * FROM suppliers", conn)
    deliveries = pd.read_sql("SELECT * FROM deliveries", conn)
    payments = pd.read_sql("SELECT * FROM payments", conn)

    conn.close()
    return suppliers, deliveries, payments


# -------------------------
# KPI Calculations
# -------------------------
def calculate_kpis(deliveries, payments):
    # On-time delivery
    deliveries["on_time"] = deliveries["delivery_date"] <= deliveries["expected_date"]
    on_time_rate = round(deliveries["on_time"].mean() * 100, 2)

    # Invoice accuracy
    invoice_accuracy = round(deliveries["invoice_correct"].mean() * 100, 2)

    # Invoice rejection rate
    rejection_rate = round(deliveries["is_rejected"].mean() * 100, 2)

    # Average payment days
    payments["payment_days"] = (
        pd.to_datetime(payments["paid_date"]) -
        pd.to_datetime(payments["due_date"])
    ).dt.days
    avg_payment_days = round(payments["payment_days"].mean(), 2)

    # Average outstanding amount
    avg_outstanding = round(payments["outstanding_amount"].mean(), 2)

    return {
        "On-Time Delivery (%)": on_time_rate,
        "Invoice Accuracy (%)": invoice_accuracy,
        "Invoice Rejection Rate (%)": rejection_rate,
        "Avg Payment Days": avg_payment_days,
        "Avg Outstanding Amount": avg_outstanding
    }
