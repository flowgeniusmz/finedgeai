import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 7
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)

# Mock Data
deal_origination_data = pd.DataFrame({
    'Deal Name': ['Deal A', 'Deal B', 'Deal C', 'Deal D'],
    'Stage': ['Origination', 'Due Diligence', 'Negotiation', 'Closed'],
    'Potential Profit ($)': [1_000_000, 1_500_000, 2_000_000, 2_500_000],
    'Partnership Split (%)': [30, 40, 50, 60],
    'Progress (%)': [20, 50, 70, 100]
})

# Frontend
st.title("Origination Deal Tracker")

# Display Deal Origination Data
st.subheader("Deal Origination Data")
st.dataframe(deal_origination_data)

# Deal Progress Visualization
fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(deal_origination_data['Deal Name'], deal_origination_data['Progress (%)'], color='blue')
ax.set_xlabel('Progress (%)')
ax.set_title('Deal Progress')

st.pyplot(fig)

# Display Potential Profits and Partnership Splits
st.subheader("Potential Profits and Partnership Splits")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.bar(deal_origination_data['Deal Name'], deal_origination_data['Potential Profit ($)'], color='green')
ax1.set_title('Potential Profit ($)')
ax1.set_ylabel('Profit ($)')

ax2.bar(deal_origination_data['Deal Name'], deal_origination_data['Partnership Split (%)'], color='orange')
ax2.set_title('Partnership Split (%)')
ax2.set_ylabel('Split (%)')

st.pyplot(fig)
