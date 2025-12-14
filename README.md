# Supplier SLA Dashboard

## Project Overview
The Supplier SLA Dashboard is an interactive analytics application that monitors supplier performance using key SLA metrics such as on-time delivery, invoice accuracy, invoice rejection rate, average payment days, and outstanding amounts. The dashboard helps procurement and finance teams evaluate supplier reliability and compliance.

---

## Problem Statement
Organizations work with multiple suppliers and need a simple way to track whether suppliers meet agreed Service Level Agreements (SLAs). Manual tracking is error-prone and inefficient. This project provides an automated dashboard to calculate and visualize supplier KPIs.

---

## Project Architecture
- SQLite database stores supplier and invoice data
- Python scripts generate and load synthetic data
- KPI logic calculates performance metrics
- Streamlit dashboard visualizes KPIs interactively

---

## Folder Structure
```
Supplier_SLA_Dashboard/
│── app/
│   ├── dashboard.py
│   ├── kpi_logic.py
│
│── data/
│   └── supplier_data.db
│
│── scripts/
│   ├── create_tables.py
│   ├── generate_data.py
│
│── tests/
│   └── test_kpi_logic.py
│
│── requirements.txt
│── README.md
│── DESIGN_DOCUMENT.md

```

---

## Environment Setup
1. Install Python 3.9+
2. Create virtual environment (optional)
3. Install dependencies

```bash
pip install -r requirements.txt  
```


## How to Run the Project

1. Generate database tables
```bash
python scripts/create_tables.py
```

2. Generate sample supplier data
```bash
python scripts/generate_data.py
```

3. Run the dashboard
```bash
streamlit run app/dashboard.py
```

## Libraries Used

- pandas

- sqlite3

- streamlit

- plotly

## Sample Data Explanation

The data used in this project is synthetically generated. It includes supplier names, invoice dates, delivery dates, payment dates, invoice amounts, and status fields. The data simulates real-world supplier performance scenarios.

## KPIs Calculated

- On-Time Delivery Rate – Percentage of deliveries completed on or before the expected date

- Invoice Accuracy – Percentage of invoices without errors

- Invoice Rejection Rate – Percentage of rejected invoices

- Average Payment Days – Average time taken to pay suppliers

- Average Outstanding Amount – Average unpaid invoice amount
