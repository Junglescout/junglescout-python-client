from enum import Enum


class ProductSort(Enum):
    """Enum class representing the sorting options for products.

    Each option is represented by a string value prefixed with a hyphen (-).
    """

    NAME = "-name"
    CATEGORY = "-category"
    REVENUE = "-revenue"
    SALES = "-sales"
    PRICE = "-price"
    RANK = "-rank"
    REVIEWS = "-reviews"
    LQS = "-lqs"
    SELLERS = "-sellers"
