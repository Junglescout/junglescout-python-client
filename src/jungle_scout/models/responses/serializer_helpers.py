from datetime import datetime


def serialize_datetime(dt: datetime) -> str:
    """Serialize a datetime object to a datetime string."""
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")


def serialize_date(dt: datetime) -> str:
    """Serialize a datetime object to a date string."""
    return dt.strftime("%Y-%m-%d")
