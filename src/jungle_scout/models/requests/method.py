from enum import Enum


class Method(Enum):
    """Enumeration representing HTTP methods.

    Attributes:
        GET: Represents the HTTP GET method.
        POST: Represents the HTTP POST method.
    """

    GET = "GET"
    POST = "POST"
