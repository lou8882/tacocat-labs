import pandas as pd

from utils import constants as c
from data import units

def transform_gear_join(df_gear: pd.DataFrame) -> pd.DataFrame:
    df_gear = df_gear.rename(columns={'id': 'gear_id', 'name':'bike_name'})
    df_gear = df_gear[['gear_id','bike_name']]
    return df_gear

def transform_athlete_summary(df_athlete: pd.DataFrame) -> pd.DataFrame:

    # filter down columns
    df = df_athlete[c.athlete_summary_fields.keys()]

    # 
    df['created_at'] = pd.to_datetime(df['created_at'],format="%Y-%m-%dT%H:%M:%SZ").dt.strftime('%b %d, %Y')

    df = df.rename(columns=c.athlete_summary_fields)
    df.set_index('name', inplace=True)

    return df

def transform_gear_summary(df_gear: pd.DataFrame) -> pd.DataFrame:

    # filter down columns
    df = df_gear[c.bikes_summary_fields.keys()]

    # make data more readable
    df.round({'converted_distance':0})
    df = df.rename(columns=c.bikes_summary_fields)

    # remove index from table by setting as first value
    df.set_index('name', inplace=True)
    return df

def transform_activity(df: pd.DataFrame) -> pd.DataFrame:
    
    # filter down columns
    df = df[c.activities_fields.keys()]

    # convert units for readability
    for col in c.activities_fields.keys():
        df[col] = units.unit_convert(df, col)
    
    # rename columns for readability
    # df = df.rename(columns=c.activities_fields)
    return df
