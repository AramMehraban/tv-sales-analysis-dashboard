import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# PAGE CONFIG (must be first)
# -------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("data/advertising.csv")

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

st.markdown("---")

# -------------------------
# KPIs
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", round(df_filtered["Sales"].sum(), 2))
col2.metric("Average Sales", round(df_filtered["Sales"].mean(), 2))
col3.metric("Max Sales", round(df_filtered["Sales"].max(), 2))

st.markdown("---")

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
    template="plotly_white"
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
    template="plotly_white"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# CHART 3 - CORRELATION HEATMAP (FIXED)
# -------------------------
st.subheader("Correlation Matrix")

corr = df_filtered.corr(numeric_only=True)

fig3 = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",         
    color_continuous_scale="RdBu_r",
)

fig3.update_layout(
    width=900,
    height=600              
)

st.plotly_chart(fig3, use_container_width=True)