import streamlit as st
import plotly.express as px
from kpi_logic import load_data, calculate_kpis

st.set_page_config(page_title="Supplier SLA Dashboard", layout="wide")
st.title("📊 Supplier Performance & SLA Dashboard")

suppliers, deliveries, payments = load_data()

supplier_names = suppliers["supplier_name"].unique()
selected = st.sidebar.multiselect("Select Supplier", supplier_names, default=supplier_names)

deliveries = deliveries.merge(suppliers, on="supplier_id")
payments = payments.merge(suppliers, on="supplier_id")

deliveries = deliveries[deliveries["supplier_name"].isin(selected)]
payments = payments[payments["supplier_name"].isin(selected)]

kpis = calculate_kpis(deliveries, payments)

cols = st.columns(5)
for col, (k,v) in zip(cols, kpis.items()):
    col.metric(k, v)

st.subheader("On-Time vs Late Deliveries")
deliveries["status"] = deliveries["delivery_date"] > deliveries["expected_date"]
fig = px.histogram(deliveries, x="supplier_name", color="status", barmode="group")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Detailed Data")
st.dataframe(deliveries)

st.download_button(
    "Download CSV",
    deliveries.to_csv(index=False),
    "supplier_report.csv"
)
