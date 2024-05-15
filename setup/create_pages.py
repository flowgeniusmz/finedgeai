import os
import toml

# Load the secrets.toml file
secrets = toml.load("secrets.toml")

# Extract relevant information
page_paths = secrets["pageconfig"]["page_paths"]
page_titles = secrets["pageconfig"]["page_titles"]

# Ensure the pages directory exists
pages_dir = "pages"
os.makedirs(pages_dir, exist_ok=True)

# Template for the content of each page
page_template = """import streamlit as st

st.title("{title}")
st.header("Overview")

# Add content here
"""

# Create a Python file for each page
for path, title in zip(page_paths, page_titles):
    content = page_template.format(title=title)
    
    with open(path, "w") as file:
        file.write(content)

print("Pages created successfully.")
