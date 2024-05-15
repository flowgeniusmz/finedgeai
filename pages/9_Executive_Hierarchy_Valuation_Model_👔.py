import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 8
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)

# Mock Data
executive_role_data = pd.DataFrame({
    'Role': ['CEO', 'CFO', 'COO', 'Head of Sales'],
    'Base Salary ($)': [500_000, 400_000, 350_000, 300_000],
    'Bonus (%)': [50, 40, 35, 60],
    'Value to Company (%)': [30, 25, 20, 35]
})

# Frontend
st.title("Executive Hierarchy Valuation Model")

# Input Executive Role Data
st.sidebar.header("Input Executive Role Data")
role = st.sidebar.selectbox("Role", executive_role_data['Role'])
base_salary = st.sidebar.number_input("Base Salary ($)", min_value=100_000, value=300_000, step=50_000)
bonus_percentage = st.sidebar.number_input("Bonus (%)", min_value=0, max_value=100, value=50, step=5)
value_to_company = st.sidebar.number_input("Value to Company (%)", min_value=0, max_value=100, value=30, step=5)

# Backend Valuation Calculation
def calculate_role_value(base_salary, bonus_percentage, value_to_company):
    total_compensation = base_salary + (base_salary * bonus_percentage / 100)
    role_value = total_compensation * (value_to_company / 100)
    return total_compensation, role_value

total_compensation, role_value = calculate_role_value(base_salary, bonus_percentage, value_to_company)

# Display Valuation Results
st.subheader("Valuation Results")
st.write(f"Total Compensation: ${total_compensation:,.2f}")
st.write(f"Role Value to Company: ${role_value:,.2f}")

# Comparative Analysis with Other Roles
st.subheader("Comparative Analysis with Other Roles")
st.dataframe(executive_role_data)

# Comparison Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.bar(executive_role_data['Role'], executive_role_data['Base Salary ($)'], color='purple')
ax1.set_title('Base Salary by Role')
ax1.set_ylabel('Base Salary ($)')

ax2.bar(executive_role_data['Role'], executive_role_data['Value to Company (%)'], color='red')
ax2.set_title('Value to Company by Role')
ax2.set_ylabel('Value to Company (%)')

st.pyplot(fig)
