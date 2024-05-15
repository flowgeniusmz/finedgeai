import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 1
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)

def assess_risk(economic_risk, disaster_risk, market_risk, risk_factor_data):
    combined_risk = (economic_risk * risk_factor_data.loc[0, 'Impact'] +
                     disaster_risk * risk_factor_data.loc[1, 'Impact'] +
                     market_risk * risk_factor_data.loc[2, 'Impact'])
    return combined_risk

def adjust_losses(historical_loss_data, combined_risk):
    historical_loss_data['Adjusted Loss'] = historical_loss_data['Loss'] * combined_risk
    return historical_loss_data

def generate_mock_data():
    historical_loss_data = pd.DataFrame({
        'Year': range(2000, 2020),
        'Loss': np.random.normal(1000000, 200000, 20)
    })
    actuarial_tables = pd.DataFrame({
        'Age': range(20, 71),
        'Risk': np.random.random(51)
    })
    risk_factor_data = pd.DataFrame({
        'Factor': ['Economic', 'Natural Disaster', 'Market Volatility'],
        'Impact': [0.3, 0.5, 0.2]
    })
    return historical_loss_data, actuarial_tables, risk_factor_data

# Mock Data
historical_loss_data = pd.DataFrame({
    'Year': range(2000, 2020),
    'Loss': np.random.normal(1000000, 200000, 20)
})
actuarial_tables = pd.DataFrame({
    'Age': range(20, 71),
    'Risk': np.random.random(51)
})
risk_factor_data = pd.DataFrame({
    'Factor': ['Economic', 'Natural Disaster', 'Market Volatility'],
    'Impact': [0.3, 0.5, 0.2]
})

# Frontend
st.title("Risk Analysis and Visualization Tool")

st.sidebar.header("Input Risk Factors")
economic_risk = st.sidebar.slider("Economic Risk", 0.0, 1.0, 0.3)
disaster_risk = st.sidebar.slider("Natural Disaster Risk", 0.0, 1.0, 0.5)
market_risk = st.sidebar.slider("Market Volatility Risk", 0.0, 1.0, 0.2)

# Risk Assessment Function
def assess_risk(economic_risk, disaster_risk, market_risk):
    combined_risk = (economic_risk * risk_factor_data.loc[0, 'Impact'] +
                     disaster_risk * risk_factor_data.loc[1, 'Impact'] +
                     market_risk * risk_factor_data.loc[2, 'Impact'])
    return combined_risk

# Data Processing and Analytics
combined_risk = assess_risk(economic_risk, disaster_risk, market_risk)
historical_loss_data['Adjusted Loss'] = historical_loss_data['Loss'] * combined_risk

# Visualization
st.subheader("Risk Assessment Results")
st.write(f"Combined Risk Factor: {combined_risk:.2f}")

fig, ax = plt.subplots()
ax.plot(historical_loss_data['Year'], historical_loss_data['Adjusted Loss'], label='Adjusted Loss')
ax.set_xlabel('Year')
ax.set_ylabel('Adjusted Loss ($)')
ax.set_title('Adjusted Loss Over Time')
ax.legend()

st.pyplot(fig)

st.subheader("Historical Loss Data")
st.write(historical_loss_data)

st.subheader("Actuarial Tables")
st.write(actuarial_tables)

st.subheader("Risk Factor Data")
st.write(risk_factor_data)
