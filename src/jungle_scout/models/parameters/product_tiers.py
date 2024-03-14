from enum import Enum


class ProductTiers(Enum):
    """Enum representing the different product tiers.

    Attributes:
        OVERSIZE (str): Represents the oversize product tier.
        STANDARD (str): Represents the standard product tier.
    """

    OVERSIZE = "oversize"
    STANDARD = "standard"
