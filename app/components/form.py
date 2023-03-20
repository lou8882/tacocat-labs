import streamlit as st
from streamlit import session_state as session

from utils import constants as c
from components import pages, buttons

def sidebar():
    st.sidebar.write("Show me some data!")
    btns = {}
    btns["table"] = st.sidebar.button("Table Maker",on_click=buttons.table_maker)
    # btns["table"] = st.sidebar.button("Data Table")
    # btns["line"] = st.sidebar.button("Line Chart")
    return btns
