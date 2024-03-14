from enum import Enum


class ApiType(Enum):
    """
    Represents the type of API used by the Jungle Scout Python client.

    Attributes:
        JS (str): The Jungle Scout API.
        COBALT (str): The Cobalt API.
    """

    JS = "junglescout"
    COBALT = "cobalt"
