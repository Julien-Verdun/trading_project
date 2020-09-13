import time


def date_to_timestamp(date):
    """
    Converts a date, format 2020-01-23
    to a timestamp, format 12322342
    """
    return time.mktime(time.strptime(date, "%Y-%m-%d"))


def timestamp_to_date(timestamp):
    """
    Converts a timestamp, format 13134234
    to a date, format 2020-01-23
    """
    return time.strftime("%Y-%m-%d", time.gmtime(timestamp))


def increase_date(date, i=0):
    """
    Takes a date, format 2020-01-23, and increases this date of i days
    Returns a date, format 2020-01-23 plus i days
    """
    return timestamp_to_date(date_to_timestamp(date) + i * 24*3600)
