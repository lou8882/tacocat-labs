import time, datetime

def get_now_epoch() -> float:
    return time.time()


def get_year_epochs(year: float) -> list[float]:

    begin = datetime.datetime(year,1,1,0,0).timestamp()
    end = datetime.datetime(year+1,1,1,0,0).timestamp() - 1
    return [begin,end]