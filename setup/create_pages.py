import os

# List of page paths from the `secrets.toml` file
page_paths = [
    "pages/1_Home_🏠.py", 
    "pages/2_Risk_Analysis_Tool_📊.py", 
    "pages/3_Reinsurance_Network_Simulation_🔢.py", 
    "pages/4_Investment_Banking_Profit_Calculator_💰.py", 
    "pages/5_Sales_Performance_Analyzer_📈.py", 
    "pages/6_Insurance_Product_Lifecycle_Management_🔍.py", 
    "pages/7_Income_Stream_Valuation_Tool_💵.py", 
    "pages/8_Origination_Deal_Tracker_🔍.py", 
    "pages/9_Executive_Hierarchy_Valuation_Model_👔.py", 
    "pages/10_Investment_Banking_Career_Advisor_🗂.py", 
    "pages/11_Financial_Product_Return_Simulator_📊.py"
]

# Directory to create the pages in
pages_dir = "pages"

# Ensure the directory exists
os.makedirs(pages_dir, exist_ok=True)

# Template for the content of each page
page_template = """import streamlit as st

st.title("{title}")
st.header("Overview")

# Add content here
"""

# Dictionary to map file names to titles
titles = {
    "1_Home_🏠.py": "Home",
    "2_Risk_Analysis_Tool_📊.py": "Risk Analysis Tool",
    "3_Reinsurance_Network_Simulation_🔢.py": "Reinsurance Network Simulation",
    "4_Investment_Banking_Profit_Calculator_💰.py": "Investment Banking Profit Calculator",
    "5_Sales_Performance_Analyzer_📈.py": "Sales Performance Analyzer",
    "6_Insurance_Product_Lifecycle_Management_🔍.py": "Insurance Product Lifecycle Management",
    "7_Income_Stream_Valuation_Tool_💵.py": "Income Stream Valuation Tool",
    "8_Origination_Deal_Tracker_🔍.py": "Origination Deal Tracker",
    "9_Executive_Hierarchy_Valuation_Model_👔.py": "Executive Hierarchy Valuation Model",
    "10_Investment_Banking_Career_Advisor_🗂.py": "Investment Banking Career Advisor",
    "11_Financial_Product_Return_Simulator_📊.py": "Financial Product Return Simulator"
}

# Create a Python file for each page
for path in page_paths:
    filename = os.path.basename(path)
    title = titles.get(filename, "Untitled Page")
    content = page_template.format(title=title)
    
    with open(path, "w") as file:
        file.write(content)

print("Pages created successfully.")
