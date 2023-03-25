import streamlit as st
from streamlit import session_state as session
import altair as alt
import pandas as pd

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

    st.image(session.auth.athlete["profile"])
    st.title(f"Table maker for {session.auth.athlete['firstname']}")

    # opts = [y for y in session.datamaker.years.keys()]
    # opts.sort(reverse=True)
    opts = sorted(session.datamaker.years.keys(), reverse=True)
    session.year_selector = st.selectbox(label="year selector",options=opts)
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

    # fill year selector dropdown with all years since user has created acct
    opts = sorted(session.datamaker.years.keys(), reverse=True)
    session.year_selector = st.multiselect(label="year selector",options=opts)
    # session.stat_selector = st.selectbox(label="stat selector", options=["distance","elapsed_time"])
    session.stat_selector = "distance"
    buttons.create_line_button()

def line_page():
    session.sidebar = buttons.sidebar()
    st.image(session.auth.athlete["profile"])
    st.title(f"Results {str(session.year_selector)}")

    df = session.datamaker.get_line_chart_df(session.year_selector, session.stat_selector)
    df = df.rename(columns=c.activities_fields)
    chart = alt.Chart(df).mark_line().encode(x=f'{c.activities_fields["start_date_local"]}:T',y=f'{c.activities_fields[session.stat_selector]}:Q')
    # chart = alt_chart(df)
    st.altair_chart(chart, use_container_width=True)


    # st.dataframe(df,use_container_width=True)
    buttons.home_button()
    buttons.line_maker_button("Back to Line Chart Maker")

#####

def alt_chart(df: pd.DataFrame): 

# chart made based on code found here
# https://altair-viz.github.io/gallery/line_chart_with_custom_legend.html

    base =  alt.Chart(df).encode(
        color=alt.Color(c.activities_fields["start_date_local"], legend=None)
    ).properties(width=500)

    line = base.mark_line().encode(x=c.activities_fields["start_date_local"],y='distance')

    last_date = base.mark_circle().encode(
        x=alt.X("last_date['activity date']:T"),
        y=alt.Y("last_date['distance']:Q")
    ).transform_aggregate(
        last_date="argmax(activity date)",
        groupby=["year"]
    )

    year = last_date.mark_text(align="left", dx=4).encode(text='year')

    chart = (line + last_date + year).encode(
        x=alt.X(title="date"),
        y=alt.Y(title="miles")
    )
    return chart