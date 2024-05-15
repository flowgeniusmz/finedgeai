import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import pagesetup as ps, sessionstates as ss


# 0. Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
page = 9
ps.master_page_display_styled_popmenu_pop(varPageNumber=page)

# Mock Data
career_progression_data = pd.DataFrame({
    'Role': ['Analyst', 'Associate', 'VP', 'Director', 'Managing Director'],
    'Years Experience': [1, 3, 5, 10, 15],
    'Average Salary ($)': [100_000, 150_000, 200_000, 300_000, 500_000],
    'Benefits': ['Training', 'Bonus', 'Stock Options', 'Profit Sharing', 'Executive Perks']
})

# Frontend
st.title("Investment Banking Career Advisor")

# Input Career Parameters
st.sidebar.header("Input Career Parameters")
experience_years = st.sidebar.slider("Years of Experience", min_value=0, max_value=20, value=5, step=1)

# Backend Career Advice
def get_career_advice(experience_years):
    role = career_progression_data[career_progression_data['Years Experience'] <= experience_years]['Role'].values[-1]
    salary = career_progression_data[career_progression_data['Years Experience'] <= experience_years]['Average Salary ($)'].values[-1]
    benefits = career_progression_data[career_progression_data['Years Experience'] <= experience_years]['Benefits'].values[-1]
    return role, salary, benefits

role, salary, benefits = get_career_advice(experience_years)

# Display Career Advice
st.subheader("Career Advice")
st.write(f"Recommended Role: {role}")
st.write(f"Expected Salary: ${salary:,.2f}")
st.write(f"Benefits: {benefits}")

# Display Career Progression Data
st.subheader("Career Progression Data")
st.dataframe(career_progression_data)

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(career_progression_data['Years Experience'], career_progression_data['Average Salary ($)'], marker='o')
ax.set_title('Career Progression')
ax.set_xlabel('Years Experience')
ax.set_ylabel('Average Salary ($)')

st.pyplot(fig)
