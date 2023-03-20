import streamlit as st
from streamlit import session_state as session
import altair as alt

from utils import auth
from utils import constants as c
from components import buttons, form
from data import transformers


def welcome_page():
    st.title("Welcome to Tacocat Laboratories")
    st.image(c.tacocat_image_url)
    st.write(f"[Click here to log into your Strava account]({session.auth.auth_url})")

def home_page():
    session.sidebar = buttons.sidebar()
    st.title("Welcome to Taco's Lab")
    st.image(session.auth.athlete["profile"])
    st.subheader("Everything there is to know about you!")

    # athlete summary table
    st.dataframe(transformers.transform_athlete_summary(session.datamaker.athlete)[0:1])

    st.subheader("Your gear")
    # gear summary table
    st.dataframe(transformers.transform_gear_summary(session.datamaker.gear))

    
def invalid_permissions_page(message:str):
    st.title("There was an error")
    st.image(c.sadbear_image_url)
    st.subheader(message)
    st.write(f"[Click here to try again]({session.auth.auth_url})")

def error_page(error):
    st.image(c.sadbear_image_url)
    st.write(error)
    st.write(f"[There was an unknown error, click here to log back in and try again]({session.auth.auth_url})")

def table_maker_page():
    session.sidebar = buttons.sidebar()
    # print(session.auth.access_token)

    st.image(session.auth.athlete["profile"])
    st.title(f"Table maker for {session.auth.athlete['firstname']}")

    session.year_selector = st.selectbox(label="year selector",options=[2023,2022,2021,2020])
    buttons.create_table_button()


def table_page():
    session.sidebar = buttons.sidebar()
    st.image(session.auth.athlete["profile"])
    st.title(f"Results {str(session.year_selector)}")
    df = session.datamaker.years[session.year_selector].rename(columns=c.activities_fields)
    st.dataframe(df,use_container_width=True)
    buttons.home_button()
    buttons.table_maker_button("Back to Table Maker")


def line_maker_page():
    session.sidebar = buttons.sidebar()
    st.image(session.auth.athlete["profile"])
    st.title(f"Line Chart Maker for {session.auth.athlete['firstname']}")
    session.year_selector = st.selectbox(label="year selector",options=[2023,2022,2021])
    # session.stat_selector = st.selectbox(label="stat selector", options=["distance","elapsed_time"])
    session.stat_selector = "distance"
    buttons.create_line_button()

def line_page():
    session.sidebar = buttons.sidebar()
    st.image(session.auth.athlete["profile"])
    st.title(f"Results {str(session.year_selector)}")
    # df = session.datamaker.years[session.year_selector]
    df = session.datamaker.get_line_chart_df(session.year_selector, session.stat_selector)
    df = df.rename(columns=c.activities_fields)
    chart = alt.Chart(df).mark_line().encode(x=f'{c.activities_fields["start_date_local"]}:T',y=f'{c.activities_fields[session.stat_selector]}:Q')
    st.altair_chart(chart, use_container_width=True)


    # st.dataframe(df,use_container_width=True)
    buttons.home_button()
    buttons.line_maker_button("Back to Line Chart Maker")