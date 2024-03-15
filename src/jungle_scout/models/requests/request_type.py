from enum import Enum


class RequestType(Enum):
    KEYWORDS_BY_ASIN = "keywords_by_asin_query"
    KEYWORDS_BY_KEYWORD = "keywords_by_keyword_query"
    HISTORICAL_SEARCH_VOLUME = "historical_search_volume"
    SALES_ESTIMATES = "sales_estimates_query"
    SHARE_OF_VOICE = "share_of_voice"
    PRODUCT_DATABASE = "product_database_query"
