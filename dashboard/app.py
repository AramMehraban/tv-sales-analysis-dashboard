import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# Load Data
# -------------------------
df = pd.read_csv("data/advertising.csv")

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# -------------------------
# SIDEBAR FILTERS
# -------------------------
st.sidebar.title("Filters")

min_sales = int(df["Sales"].min())
max_sales = int(df["Sales"].max())

sales_filter = st.sidebar.slider(
    "Sales Range",
    min_sales,
    max_sales,
    (min_sales, max_sales)
)

df_filtered = df[
    (df["Sales"] >= sales_filter[0]) &
    (df["Sales"] <= sales_filter[1])
]

# -------------------------
# TITLE
# -------------------------
st.title("Sales Analytics Dashboard (Power BI Style)")

# -------------------------
# KPIs
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", round(df_filtered["Sales"].sum(), 2))
col2.metric("Average Sales", round(df_filtered["Sales"].mean(), 2))
col3.metric("Max Sales", round(df_filtered["Sales"].max(), 2))

# -------------------------
# CHART 1 - Scatter
# -------------------------
st.subheader("TV Advertising vs Sales")

fig1 = px.scatter(
    df_filtered,
    x="TV",
    y="Sales",
    color="Sales",
    size="Sales",
    title="TV vs Sales Relationship"
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------
# CHART 2 - Bar Chart
# -------------------------
st.subheader("Sales Distribution")

fig2 = px.bar(
    df_filtered,
    x=df_filtered.index,
    y="Sales",
    title="Sales per Observation"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# CHART 3 - Correlation Heatmap
# -------------------------
st.subheader("Correlation Matrix")

corr = df_filtered.corr()

fig3 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap"
)

st.plotly_chart(fig3, use_container_width=True)
