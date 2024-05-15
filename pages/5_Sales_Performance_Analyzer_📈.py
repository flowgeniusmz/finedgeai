import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 4
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)

# Mock Data
sales_performance_data = pd.DataFrame({
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David'],
    'Revenue Generated': [1_200_000, 950_000, 1_500_000, 1_100_000],
    'Deals Closed': [15, 10, 20, 12],
    'Efficiency (%)': [80, 75, 85, 78]
})

# Frontend
st.title("Sales Performance Analyzer for Investment Banking")

# Display Sales Performance Metrics
st.subheader("Sales Performance Metrics")
st.dataframe(sales_performance_data)

# Performance Analysis
def analyze_performance(data):
    average_revenue = data['Revenue Generated'].mean()
    total_deals_closed = data['Deals Closed'].sum()
    average_efficiency = data['Efficiency (%)'].mean()
    return average_revenue, total_deals_closed, average_efficiency

average_revenue, total_deals_closed, average_efficiency = analyze_performance(sales_performance_data)

# Display Analysis Results
st.subheader("Performance Analysis")
st.write(f"Average Revenue Generated: ${average_revenue:,.2f}")
st.write(f"Total Deals Closed: {total_deals_closed}")
st.write(f"Average Efficiency: {average_efficiency:.2f}%")

# Visualization
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].bar(sales_performance_data['Salesperson'], sales_performance_data['Revenue Generated'], color='skyblue')
ax[0].set_title('Revenue Generated by Salesperson')
ax[0].set_ylabel('Revenue ($)')

ax[1].bar(sales_performance_data['Salesperson'], sales_performance_data['Efficiency (%)'], color='green')
ax[1].set_title('Efficiency by Salesperson')
ax[1].set_ylabel('Efficiency (%)')

st.pyplot(fig)
