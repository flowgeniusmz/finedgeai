import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 5
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)

# Mock Data
insurance_product_data = pd.DataFrame({
    'Product': ['Term Life', 'Whole Life', 'Universal Life', 'Variable Life'],
    'Origination Date': pd.to_datetime(['2015-01-01', '2016-06-15', '2017-09-30', '2018-11-20']),
    'Payout Date': pd.to_datetime(['2025-01-01', '2046-06-15', '2057-09-30', '2068-11-20']),
    'Risk Assessment': [0.1, 0.2, 0.15, 0.25],
    'Profit': [500_000, 1_000_000, 750_000, 1_200_000]
})

# Frontend
st.title("Insurance Product Lifecycle Management")

# Display Insurance Product Data
st.subheader("Insurance Product Data")
st.dataframe(insurance_product_data)

# Lifecycle Management
def manage_lifecycle(data):
    current_date = pd.to_datetime('today')
    data['Current Status'] = np.where(data['Payout Date'] > current_date, 'Active', 'Matured')
    return data

managed_data = manage_lifecycle(insurance_product_data)

# Display Managed Data
st.subheader("Managed Insurance Product Data")
st.dataframe(managed_data)

# Visualization
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].pie(managed_data['Risk Assessment'], labels=managed_data['Product'], autopct='%1.1f%%')
ax[0].set_title('Risk Assessment Distribution')

ax[1].bar(managed_data['Product'], managed_data['Profit'], color='purple')
ax[1].set_title('Profit by Product')
ax[1].set_ylabel('Profit ($)')

st.pyplot(fig)
