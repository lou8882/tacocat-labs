import pandas as pd


mps_to_mph = ['average_speed','max_speed']
temp_cel_to_fh = ['average_temp']
meters_to_feet = ['total_elevation_gain']
meters_to_miles = ['distance']
seconds_to_hhmm = ['elapsed_time']
datetime_to_mmddyyhhmm = ['start_date_local']
other_round_numbers = ['average_cadence','average_watts','kilojoules','average_heartrate','max_heartrate','suffer_score']

def unit_convert(df: pd.DataFrame, col: str) -> pd.DataFrame:
    if col in mps_to_mph:
        ret = df[col].fillna(0)
        ret = ret * 2.23694
        return ret.round(2)

    elif col in temp_cel_to_fh:
        ret = df[col].fillna(0)
        ret = ret * 1.8 + 32
        return ret.astype(int)

    elif col in meters_to_feet:
        ret = df[col].fillna(0)
        ret = ret * 3.28084
        return ret.astype(int)

    elif col in meters_to_miles:
        ret = df[col].fillna(0)
        ret = ret.astype(int)
        ret = ret / 1609.34
        return ret.round(2)

    elif col in seconds_to_hhmm:
        ret = pd.to_timedelta(df[col],unit='s')
        return [time_hhmmss_format(x) for x in ret]

    elif col in datetime_to_mmddyyhhmm:
        # return pd.to_datetime(df[col],format="%Y-%m-%dT%H:%M:%SZ").dt.strftime('%b %d, %Y %I:%M%p')
        return pd.to_datetime(df[col],format="%Y-%m-%dT%H:%M:%SZ")

    elif col in other_round_numbers:
        ret = df[col].fillna(0)
        return ret.astype(int)
        
    else:
        return df[col]

def time_hhmmss_format(x:pd.Timedelta):
    days = x.days
    hours, remain = divmod(x.seconds , 3600)
    str_hours = str((days * 24) + hours)
    minutes, seconds = divmod(remain , 60)
    str_mins = str(minutes)
    str_sec = str(seconds)
    if hours > 0:
        return f'{str_hours}h {str_mins}m {str_sec}s'
    else:
        return f'{str_mins}m {str_sec}s'
