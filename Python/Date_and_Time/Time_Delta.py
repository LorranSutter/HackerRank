import datetime as dt

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'

    t1 = dt.datetime.strptime(t1,fmt)
    t2 = dt.datetime.strptime(t2,fmt)

    return str(int(abs(t1-t2).total_seconds()))