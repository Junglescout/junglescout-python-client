from enum import Enum


class SellerTypes(Enum):
    """Enum class representing different types of sellers.

    Attributes:
        - AMZ: Represents the Amazon seller type.
        - FBA: Represents the Fulfilled by Amazon (FBA) seller type.
        - FBM: Represents the Fulfilled by Merchant (FBM) seller type.
    """

    AMZ = "amz"
    FBA = "fba"
    FBM = "fbm"
