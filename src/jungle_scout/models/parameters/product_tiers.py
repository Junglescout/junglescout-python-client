from enum import Enum


class ProductTiers(Enum):
    """Enum representing the different product tiers.

    Attributes:
        - OVERSIZE: Represents the oversize product tier.
        - STANDARD: Represents the standard product tier.
    """

    OVERSIZE = "oversize"
    STANDARD = "standard"
