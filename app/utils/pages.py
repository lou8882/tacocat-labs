import streamlit as st

from utils import auth
from utils import constants as c
from data import transformers


def welcome_page():
    st.title("Welcome to Tacocat Laboratories")
    st.image(c.tacocat_image_url)
    st.write(f"[Click here to log into your Strava account]({st.session_state.auth.auth_url})")

def home_page():
    btns = sidebar()
    st.title("Welcome to Taco's Lab")
    st.image(st.session_state.auth.athlete["profile"])
    st.subheader("Everything there is to know about you!")

    # athlete summary table
    st.dataframe(transformers.transform_athlete_summary(st.session_state.datamaker.athlete)[0:1])

    st.subheader("Your gear")
    # gear summary table
    st.dataframe(transformers.transform_gear_summary(st.session_state.datamaker.gear))

    if btns["table"]:
        st.session_state["page"] = c.table
        table_page()
    
def invalid_permissions_page(message:str):
    st.title("There was an error")
    st.image(c.sadbear_image_url)
    st.subheader(message)
    st.write(f"[Click here to try again]({st.session_state.auth.auth_url})")

def error_page(error):
    st.image(c.sadbear_image_url)
    st.write(error)
    st.write(f"[There was an unknown error, click here to log back in and try again]({st.session_state.auth.auth_url})")

def sidebar():
    st.sidebar.write("Show me some data!")
    btns = {}
    btns["table"] = st.sidebar.button("Table Maker")
    # btns["table"] = st.sidebar.button("Data Table")
    # btns["line"] = st.sidebar.button("Line Chart")
    return btns

def table_page():
    print(st.session_state.auth.access_token)
    year_selector = st.session_state.inputs.year if 'inputs' in st.session_state else None
    # btns = sidebar()
    st.image(st.session_state.auth.athlete["profile"])
    st.title(f"Table maker for {st.session_state.auth.athlete['firstname']}")
    # selectors = {'year':}
    year_selector = st.selectbox(label="year selector",options=[2023,2022,2021,2020])
    create_table = st.button("Generate Table")

    if create_table:
        st.session_state.datamaker.fetch_activity_data(year_selector)
        st.dataframe(st.session_state.datamaker.years[year_selector],use_container_width=True)