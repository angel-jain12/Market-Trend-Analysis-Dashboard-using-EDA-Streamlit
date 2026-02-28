import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.title("📊 Market Trend Analysis Dashboard")

# Project Summary
st.header("📌 Project Summary")

st.write("""
This project focuses on analyzing sales market trends using Exploratory Data Analysis (EDA).
The goal is to identify growth patterns, high-performing regions and product demand.

The analysis helps in understanding:

- Market growth over time
- Regional performance
- Category demand

This dashboard presents key business insights derived from sales data.
""")

# Tools Used
st.header("🛠 Tools & Technologies Used")

st.write("""
- Python
- Pandas
- Matplotlib
- Streamlit
- Jupyter Notebook
""")

# Load Data
df = pd.read_csv("train.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Month'] = df['Order Date'].dt.strftime('%b')

# KPI
st.header("📈 Key Metrics")
col1, col2 = st.columns(2)
col1.metric("Total Sales", int(df['Sales'].sum()))
col2.metric("Total Orders", df.shape[0])

# Graph 1 — Monthly Trend
st.header("📅 Monthly Sales Trend")
monthly_sales = df.groupby('Month')['Sales'].sum()
fig1, ax1 = plt.subplots()
monthly_sales.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# Graph 2 — Region Performance
st.header("🌍 Sales by Region")
region_sales = df.groupby('Region')['Sales'].sum()
fig2, ax2 = plt.subplots()
region_sales.plot(kind='bar', ax=ax2)
st.pyplot(fig2)

# Graph 3 — Category Demand
st.header("🛍 Sales by Category")
category_sales = df.groupby('Category')['Sales'].sum()
fig3, ax3 = plt.subplots()
category_sales.plot(kind='bar', ax=ax3)
st.pyplot(fig3)

# Insights
st.header("💡 Key Insights")

st.write("""
- The market shows strong growth trends across months.
- Some regions outperform others in total sales contribution.
- Certain product categories dominate overall market demand.

These insights help businesses make data-driven decisions.
""")