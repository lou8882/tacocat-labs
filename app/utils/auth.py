
import os
import requests
import json
import time
import streamlit as st
from utils import constants, pages
from exceptions.exceptions import AuthException

class Auth():
    def __init__(self):
        self.client_id: str = os.getenv(constants.client_id_var)
        self.client_secret: str = os.getenv(constants.client_secret_var)
        self.auth_url: str = self.set_auth_url()

        self.code = None
        self.scope = None
        self.refresh_token = None
        self.access_token = None
        self.athlete = None
        self.expires_at = None

    def set_auth_url(self):
        if os.getenv('HOSTED_BY') == 'heroku':
            return f"http://www.strava.com/oauth/authorize?client_id={self.client_id}&response_type=code&redirect_uri=https://tacocat-labs.herokuapp.com/&scope=activity:read_all,profile:read_all"
        else:
            return f"http://www.strava.com/oauth/authorize?client_id={self.client_id}&response_type=code&redirect_uri=http://localhost:8501/&scope=activity:read_all,profile:read_all"


    def login(self, params: dict):
        # print("auth_login")
        expires = self.expires_at
        if expires:
            now = time.time()
            if now > expires:
                self.refresh_creds()
            return
        self.code: str = params['code'][0]
        self.scope: str = params['scope'][0]
        myparams = {"client_id":int(self.client_id),
            "client_secret":self.client_secret,
            "grant_type":"authorization_code",
            "code":self.code}
        
        # print(f"auth login params: {myparams}")
        r = requests.post("https://www.strava.com/oauth/token",params=myparams)
        dct = json.loads(r.text)

        if 'errors' in dct:
            raise AuthException(dct['errors'])
        
        # print(f"login dct: {dct}")
        self.refresh_token: str = dct['refresh_token']
        self.access_token: str = dct['access_token']
        self.athlete: dict = dct['athlete']
        self.expires_at: int = dct['expires_at']

    def refresh_creds(self):
        print("refresh_creds")        
        myparams = {"client_id":int(self.client_id),
            "client_secret":self.client_secret,
            "grant_type":"refresh_token",
            "code":self.refresh_token}

        print(f"auth refresh params: {myparams}")
        r = requests.post("https://www.strava.com/oauth/token",params=myparams)
        dct = json.loads(r.text)

        if dct['errors']:
            raise Exception(dct['errors'])

        print(f"refrsh dct: {dct}")
        self.access_token: str = dct['access_token']
        self.expires_at: int = dct['expires_at']

    def __str__(self):
        self_str = {}
        self_str["client_id"] = self.client_id
        self_str["client_secret"] = self.client_secret
        self_str["auth_url"] = self.auth_url
        self_str["code"] = self.code
        self_str["scope"] = self.scope
        self_str["refresh_token"] = self.refresh_token
        self_str["access_token"] = self.access_token
        self_str["athlete"] = self.athlete
        self_str["expires_at"] = self.expires_at
        return self_str