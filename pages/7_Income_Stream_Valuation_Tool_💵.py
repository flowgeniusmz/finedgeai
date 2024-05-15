import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 6
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)

# Mock Data
income_stream_data = pd.DataFrame({
    'Income Stream': ['Stream A', 'Stream B', 'Stream C', 'Stream D'],
    'Initial Investment': [100_000, 150_000, 200_000, 250_000],
    'Annual Return Rate (%)': [0.05, 0.07, 0.06, 0.08],
    'Duration (Years)': [10, 10, 10, 10]
})

# Frontend
st.title("Income Stream Valuation Tool")

# Input Income Stream Parameters
st.sidebar.header("Input Income Stream Parameters")
initial_investment = st.sidebar.number_input("Initial Investment ($)", min_value=10_000, value=100_000, step=10_000)
annual_return_rate = st.sidebar.number_input("Annual Return Rate (%)", min_value=0.01, max_value=0.20, value=0.05, step=0.01) / 100
duration = st.sidebar.number_input("Duration (Years)", min_value=1, max_value=30, value=10, step=1)

# Backend Valuation Calculation
def calculate_valuation(initial_investment, annual_return_rate, duration):
    future_value = initial_investment * ((1 + annual_return_rate) ** duration)
    return future_value

valuation = calculate_valuation(initial_investment, annual_return_rate, duration)

# Display Valuation Result
st.subheader("Valuation Result")
st.write(f"Future Value: ${valuation:,.2f}")

# Comparative Analysis
st.subheader("Comparative Analysis with Other Income Streams")
st.dataframe(income_stream_data)

# Comparison Visualization
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].bar(income_stream_data['Income Stream'], income_stream_data['Initial Investment'], color='orange')
ax[0].set_title('Initial Investment by Income Stream')
ax[0].set_ylabel('Initial Investment ($)')

ax[1].bar(income_stream_data['Income Stream'], income_stream_data['Annual Return Rate (%)'], color='blue')
ax[1].set_title('Annual Return Rate by Income Stream')
ax[1].set_ylabel('Annual Return Rate (%)')

st.pyplot(fig)
