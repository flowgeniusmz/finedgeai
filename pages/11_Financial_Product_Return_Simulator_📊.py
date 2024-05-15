import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 10
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)


# Mock Data
historical_return_data = pd.DataFrame({
    'Year': range(2010, 2021),
    'Return (%)': np.random.uniform(0.05, 0.15, size=11)
})
financial_product_models = {
    'Stocks': lambda size: np.random.normal(0.1, 0.2, size),
    'Bonds': lambda size: np.random.normal(0.05, 0.05, size),
    'Real Estate': lambda size: np.random.normal(0.07, 0.1, size)
}

# Frontend
st.title("Financial Product Return Simulator")

# Input Financial Product Parameters
st.sidebar.header("Input Financial Product Parameters")
product_type = st.sidebar.selectbox("Financial Product Type", list(financial_product_models.keys()))
initial_investment = st.sidebar.number_input("Initial Investment ($)", min_value=10_000, value=100_000, step=10_000)
duration_years = st.sidebar.number_input("Duration (Years)", min_value=1, max_value=30, value=10, step=1)

# Backend Simulation
def simulate_returns(product_type, initial_investment, duration_years):
    model = financial_product_models[product_type]
    returns = model(duration_years)
    investment_values = initial_investment * (1 + returns).cumprod()
    return investment_values

investment_values = simulate_returns(product_type, initial_investment, duration_years)

# Display Simulation Results
st.subheader("Simulation Results")
st.line_chart(investment_values)

# Display Historical Return Data
st.subheader("Historical Return Data")
st.dataframe(historical_return_data)

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(historical_return_data['Year'], historical_return_data['Return (%)'], marker='o')
ax.set_title('Historical Returns')
ax.set_xlabel('Year')
ax.set_ylabel('Return (%)')

st.pyplot(fig)
