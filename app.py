import streamlit as st
from config import pagesetup, sessionstates as ss

a = st.button("Click")
if a:
    pagesetup.switch_to_homepage()