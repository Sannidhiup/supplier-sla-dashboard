Supplier SLA Dashboard – One‑Page Design Document

1. Problem Statement:

Organizations work with multiple suppliers and need to ensure that suppliers meet agreed Service Level Agreements (SLAs). Tracking supplier performance manually using spreadsheets is time‑consuming, error‑prone, and does not scale well as the number of suppliers and invoices increases. There is a need for an automated, easy‑to‑use system that can calculate supplier performance metrics accurately and present them in a clear visual format.

The Supplier SLA Dashboard solves this problem by providing an interactive analytics dashboard that automatically calculates key supplier KPIs and helps procurement and finance teams quickly identify high‑performing and under‑performing suppliers.

2. System Architecture & Flow:

The system follows a simple, modular architecture:

1. Data Generation Layer
Synthetic supplier and invoice data is generated using Python scripts. This simulates real‑world supplier transactions such as delivery dates, invoice amounts, payment dates, and invoice status.

2. Database Layer
The generated data is stored in an SQLite database. SQLite is lightweight, easy to configure, and sufficient for small to medium analytical applications.

3. Business Logic Layer (KPI Logic)
KPI calculations are handled in a separate Python module. This layer processes raw data from the database and computes SLA metrics such as on‑time delivery rate and average payment days.

4. Presentation Layer (Dashboard UI)
A Streamlit‑based dashboard fetches KPI results and displays them using interactive tables and charts. Users can filter data by supplier and date range to analyze performance.

Overall Flow:
Data Generation → SQLite Database → KPI Calculation Logic → Streamlit Dashboard

3. Tools & Technologies Used:

Python – Core programming language for data processing and logic

SQLite – Lightweight relational database for storing supplier data

Pandas – Data manipulation and aggregation

Streamlit – Interactive web dashboard framework

Plotly – Visualization library for charts and KPIs

Git & GitHub – Version control and project hosting

4. Key KPI Logic Explanation:

The following KPIs are calculated to evaluate supplier performance:

On‑Time Delivery Rate:
Calculated as the percentage of deliveries completed on or before the expected delivery date.

Invoice Accuracy:
Measures the percentage of invoices without errors or discrepancies.

Invoice Rejection Rate:
Percentage of invoices that were rejected due to incorrect details or mismatches.

Average Payment Days:
Calculates the average number of days taken to pay suppliers after invoice generation.

Average Outstanding Amount:
Represents the average unpaid invoice amount across suppliers.

Each KPI is computed using aggregated invoice‑level data to ensure accuracy and consistency.

5. Outcome:

The Supplier SLA Dashboard provides a clear, data‑driven view of supplier performance. It helps organizations monitor SLA compliance, identify risks early, and make informed procurement decisions using interactive analytics.