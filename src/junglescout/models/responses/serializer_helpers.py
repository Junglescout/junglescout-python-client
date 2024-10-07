from datetime import datetime
from typing import Optional


def serialize_datetime(dt: Optional[datetime]) -> Optional[str]:
    """Serialize a datetime object to a datetime string."""
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f") if dt else None


def serialize_date(dt: Optional[datetime]) -> Optional[str]:
    """Serialize a datetime object to a date string."""
    return dt.strftime("%Y-%m-%d") if dt else None
