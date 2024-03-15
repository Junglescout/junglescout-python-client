from enum import Enum


class ProductSort(Enum):
    """Enum class representing the sorting options for products.

    Each option is represented by a string value prefixed with a hyphen (-).

    Attributtes:
        - NAME: Sort by name.
        - CATEGORY: Sort by category.
        - REVENUE: Sort by revenue.
        - SALES: Sort by sales.
        - PRICE: Sort by price.
        - RANK: Sort by rank.
        - REVIEWS: Sort by reviews.
        - LQS: Sort by LQS (Listing Quality Score).
        - SELLERS: Sort by sellers.
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
