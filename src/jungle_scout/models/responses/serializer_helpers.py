from datetime import datetime


def serialize_datetime(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")


def serialize_date(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d")
