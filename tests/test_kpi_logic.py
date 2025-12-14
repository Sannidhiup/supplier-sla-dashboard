import pandas as pd
import sys
import os

# Make app folder importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.kpi_logic import calculate_kpis


def test_calculate_kpis_basic():
    # Sample deliveries data
    deliveries = pd.DataFrame({
        "delivery_date": ["2024-01-01", "2024-01-05"],
        "expected_date": ["2024-01-02", "2024-01-04"],
        "invoice_correct": [1, 0],
        "is_rejected": [0, 1]
    })

    # Sample payments data
    payments = pd.DataFrame({
        "due_date": ["2024-01-01", "2024-01-01"],
        "paid_date": ["2024-01-05", "2024-01-11"],
        "outstanding_amount": [1000, 3000]
    })

    kpis = calculate_kpis(deliveries, payments)

    assert kpis["On-Time Delivery (%)"] == 50.0
    assert kpis["Invoice Accuracy (%)"] == 50.0
    assert kpis["Invoice Rejection Rate (%)"] == 50.0
    assert kpis["Avg Payment Days"] == 7.0
    assert kpis["Avg Outstanding Amount"] == 2000.0
