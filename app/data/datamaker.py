import requests
import json
import time

import pandas as pd

from utils.auth import Auth
from utils import constants as c
from utils import time as timeutil
from data import transformers, mock

class DataMaker():
    def __init__(self, auth: Auth):
        self.auth: Auth = auth
        self.years: dict = {}
        self.athlete: pd.DataFrame = None
        self.gear: pd.DataFrame = None


    def fetch_athelete_data(self) -> None:
        # url = 'https://www.strava.com/api/v3/athlete'
        # headers = {"Authorization": "Bearer {token}"}

    ###############
        r = requests.get(self.athlete_url, headers=self.auth_headers)
        # r = mock.Mock(mock.mock_athlete_data)

        self.athlete = pd.DataFrame(r.json())
        self.gear = pd.DataFrame(r.json()['bikes'])
        start_year = timeutil.datestr_to_date(r.json()["created_at"]).tm_year
        cur_year = time.gmtime(time.time()).tm_year
        for year in range(start_year,cur_year+1):
            self.years[year] = {}


    
    def fetch_activity_data(self, year: float):
        if len(self.years[year]) == 0:
            timestamps = timeutil.get_year_epochs(year)
            page = 0 
            res_len = 100

            df_gear = transformers.transform_gear_join(self.gear)
            df = pd.DataFrame()
            while res_len == 100:
                page += 1
                params = {'after':timestamps[0],'before':timestamps[1],'per_page':100,'page':page}

        ################
                r = requests.get(self.activities_url, params=params, headers=self.auth_headers)
                r.raise_for_status()
                # r = mock.Mock(mock.mock_activities_data)

                df_2 = pd.DataFrame(r.json())

                df_2 = df_2.merge(df_gear, on='gear_id', suffixes=('','_y'), how="left")
                df_2 = transformers.transform_activity(df_2)

                df = pd.concat([df, df_2], ignore_index=True)
                res_len = len(df_2) 
        
            self.years[year] = df

    def get_line_chart_df(self, year:int, y_axis:str) -> pd.DataFrame:
        df = self.years[year]
        df = df[["start_date_local",y_axis]]
        df.sort_values(by="start_date_local",inplace=True)
        df[y_axis] = df[y_axis].cumsum()
        return df

    @property
    def activities_url(self) -> str:
        return f"{c.base_url}/athlete/activities"

    @property
    def athlete_url(self) -> str:
        return f"{c.base_url}/athlete"
        
    @property
    def auth_headers(self) -> dict:
        return {"Authorization": f"Bearer {self.auth.access_token}"}
