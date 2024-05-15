import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 3
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)

# Mock Data
historical_deal_performance = pd.DataFrame({
    'Year': range(2010, 2021),
    'Deal Size': np.random.randint(50, 200, size=11) * 1_000_000,
    'Profit': np.random.randint(5, 20, size=11) * 1_000_000
})
fee_rate_data = pd.DataFrame({
    'Deal Size Range': ['50-100M', '100-150M', '150-200M'],
    'Fee Rate': [0.02, 0.015, 0.01]
})
asset_management_stats = pd.DataFrame({
    'Year': range(2010, 2021),
    'Assets Under Management (AUM)': np.random.randint(1, 5, size=11) * 1_000_000_000,
    'Return Rate (%)': np.random.uniform(0.05, 0.15, size=11)
})

# Frontend
st.title("Investment Banking Profit Calculator")

st.sidebar.header("Input Deal Parameters")
deal_size = st.sidebar.number_input("Deal Size ($)", min_value=10_000_000, value=100_000_000, step=10_000_000)
fee_rate = st.sidebar.number_input("Fee Rate (%)", min_value=0.01, max_value=0.10, value=0.02, step=0.01) / 100
aum_percentage = st.sidebar.number_input("Asset Management Percentage (%)", min_value=0.1, max_value=5.0, value=1.0, step=0.1) / 100
projected_return = st.sidebar.number_input("Projected Return (%)", min_value=0.01, max_value=0.20, value=0.10, step=0.01) / 100

# Backend Profit Calculation
def calculate_profit(deal_size, fee_rate, aum_percentage, projected_return):
    fee_income = deal_size * fee_rate
    aum = deal_size * aum_percentage
    return_income = aum * projected_return
    total_profit = fee_income + return_income
    return total_profit, fee_income, return_income

total_profit, fee_income, return_income = calculate_profit(deal_size, fee_rate, aum_percentage, projected_return)

# Display Calculated Profits
st.subheader("Calculated Profits")
st.write(f"Total Profit: ${total_profit:,.2f}")
st.write(f"Fee Income: ${fee_income:,.2f}")
st.write(f"Return Income: ${return_income:,.2f}")

# Comparative Analysis
st.subheader("Historical Deal Performance")
st.write(historical_deal_performance)

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].plot(historical_deal_performance['Year'], historical_deal_performance['Deal Size'], marker='o')
ax[0].set_title('Deal Size Over Years')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Deal Size ($)')

ax[1].plot(historical_deal_performance['Year'], historical_deal_performance['Profit'], marker='o', color='green')
ax[1].set_title('Profit Over Years')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Profit ($)')

st.pyplot(fig)

st.subheader("Fee Rate Data")
st.write(fee_rate_data)

st.subheader("Asset Management Statistics")
st.write(asset_management_stats)

# Run the Streamlit app
if __name__ == '__main__':
    st.run()
