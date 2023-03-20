import streamlit as st
from utils.auth import Auth
from data.datamaker import DataMaker
from utils import pages
from utils import constants as c
from utils import helpers
from exceptions.exceptions import AuthException

#############
# st.session_state.page = c.table

url_params = st.experimental_get_query_params()
site_pages = helpers.get_site_pages()

if 'auth' not in st.session_state: # init empty auth session
    st.session_state.auth = Auth()
if 'datamaker' not in st.session_state: # init empty datamaker
    st.session_state.datamaker = DataMaker(st.session_state.auth)

if not "code" in url_params: # bring to home page for authentication
    # pages.welcome_page()
    site_pages[c.welcome]()
        
elif url_params["scope"][0] != "read,activity:read_all,profile:read_all": # user did not provide all access
    # pages.invalid_permissions_page("Please grant all requested permissions to access content")
    site_pages[c.invalid_permissions]("Please grant all requested permissions to access content")

elif url_params: # post auth
    try: 
        st.session_state.auth.login(url_params)
        st.session_state.datamaker.fetch_athelete_data()
        # st.session_state
        if 'page' not in st.session_state:
            site_pages[c.home]() # landing page
        else:
            site_pages[st.session_state.page]() # user selected page

    except AuthException:
        pages.invalid_permissions_page("Please do not refresh your browser as this resets your session")
        