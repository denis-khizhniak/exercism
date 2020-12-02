from datetime import timedelta


def add(moment):
    gigasecond = timedelta(seconds=10**9)
    return moment + gigasecond
