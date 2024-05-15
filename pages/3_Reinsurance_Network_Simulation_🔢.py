import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 2
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)

# Mock Data
reinsurance_contract_data = pd.DataFrame({
    'Reinsurer': ['Company A', 'Company B', 'Company C', 'Company D'],
    'Capacity': [50_000_000, 100_000_000, 75_000_000, 125_000_000],
    'Premium Rate': [0.05, 0.04, 0.045, 0.03]
})
risk_distribution_models = {
    'Uniform': lambda size: np.random.uniform(0, 1, size),
    'Normal': lambda size: np.random.normal(0.5, 0.15, size),
    'Exponential': lambda size: np.random.exponential(1, size)
}
company_financials = pd.DataFrame({
    'Company': ['Company A', 'Company B', 'Company C', 'Company D'],
    'Assets': [500_000_000, 600_000_000, 700_000_000, 800_000_000],
    'Liabilities': [300_000_000, 350_000_000, 400_000_000, 450_000_000]
})

# Frontend
st.title("Reinsurance Network Simulation")

st.sidebar.header("Input Reinsurance Parameters")
total_risk = st.sidebar.number_input("Total Risk to be Reinsured", min_value=1_000_000, value=100_000_000)
distribution_model = st.sidebar.selectbox("Risk Distribution Model", list(risk_distribution_models.keys()))

# Backend Simulation
def simulate_reinsurance(total_risk, distribution_model):
    capacity = reinsurance_contract_data['Capacity'].values
    premium_rate = reinsurance_contract_data['Premium Rate'].values
    
    distribution = risk_distribution_models[distribution_model](len(capacity))
    distribution /= distribution.sum()  # Normalize to sum to 1
    risk_allocated = total_risk * distribution
    
    premiums = risk_allocated * premium_rate
    results = reinsurance_contract_data.copy()
    results['Allocated Risk'] = risk_allocated
    results['Premium'] = premiums
    
    return results

simulation_results = simulate_reinsurance(total_risk, distribution_model)

# Visualization
st.subheader("Reinsurance Network and Risk Distribution")
st.write(simulation_results)

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].pie(simulation_results['Allocated Risk'], labels=simulation_results['Reinsurer'], autopct='%1.1f%%')
ax[0].set_title('Risk Distribution')

ax[1].bar(simulation_results['Reinsurer'], simulation_results['Premium'], color='skyblue')
ax[1].set_title('Reinsurance Premiums')
ax[1].set_ylabel('Premium ($)')

st.pyplot(fig)

st.subheader("Company Financials")
st.write(company_financials)

# Run the Streamlit app
if __name__ == '__main__':
    st.run()
