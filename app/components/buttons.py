import streamlit as st
from streamlit import session_state as session

from utils import constants as c


def home_button():
    return st.button("Return home", on_click=return_home)

def return_home():
    session.page=c.home

###### Tables
def table_maker_button(message="Make a table"):
    return st.button(message, on_click=table_maker)

def table_maker():
    session['page'] = c.table_maker

def create_table_button():
    return st.button("Create Table Now", on_click=create_table)

def create_table():
    session.datamaker.fetch_activity_data([session.year_selector])
    session.page = c.table

###### Line Charts
def line_maker_button(message="Make a Line Chart"):
    return st.button(message, on_click=line_maker)

def line_maker():
    session.page=c.line_maker

def create_line_button(message="Create Chart Now"):
    return st.button(message, on_click=create_line)

def create_line():
    session.datamaker.fetch_activity_data(session.year_selector)
    session.page=c.line


def sidebar():
    btns = {}
    btns["table"] = st.sidebar.button("Make a table",on_click=table_maker)
    # btns["line"] = st.sidebar.button("Data Table")
    btns["line"] = st.sidebar.button("Line Chart", on_click=line_maker)
    return btns

