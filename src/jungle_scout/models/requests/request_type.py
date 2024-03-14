from enum import Enum


class RequestType(Enum):
    """Enum class representing different types of requests in the Jungle Scout API.

    Attributes:
        KEYWORDS_BY_ASIN (str): Request type for querying keywords by ASIN.
        KEYWORDS_BY_KEYWORD (str): Request type for querying keywords by keyword.
        HISTORICAL_SEARCH_VOLUME (str): Request type for querying historical search volume.
        SALES_ESTIMATES (str): Request type for querying sales estimates.
        SHARE_OF_VOICE (str): Request type for querying share of voice.
        PRODUCT_DATABASE (str): Request type for querying the product database.
    """

    KEYWORDS_BY_ASIN = "keywords_by_asin_query"
    KEYWORDS_BY_KEYWORD = "keywords_by_keyword_query"
    HISTORICAL_SEARCH_VOLUME = "historical_search_volume"
    SALES_ESTIMATES = "sales_estimates_query"
    SHARE_OF_VOICE = "share_of_voice"
    PRODUCT_DATABASE = "product_database_query"
