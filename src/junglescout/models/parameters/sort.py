from enum import Enum


class Sort(Enum):
    """Enum class representing the sorting options for a search query.

    Attributes:
        - NAME: Sort by name.
        - MONTHLY_TREND: Sort by monthly trend.
        - MONTHLY_SEARCH_VOLUME_EXACT_MATCH: Sort by monthly search volume (exact match).
        - QUARTERLY_TREND: Sort by quarterly trend.
        - MONTHLY_SEARCH_VOLUME_BROAD: Sort by monthly search volume (broad match).
        - DOMINANT_CATEGORY: Sort by dominant category.
        - RECOMMENDED_PROMOTIONS: Sort by recommended promotions.
        - SP_BRAND_AD_BID: Sort by Sponsored Brand ad bid.
        - PPC_BID_BROAD: Sort by PPC bid (broad match).
        - PPC_BID_EXACT: Sort by PPC bid (exact match).
        - EASE_OF_RANKING_SCORE: Sort by ease of ranking score.
        - RELEVANCY_SCORE: Sort by relevancy score.
        - ORGANIC_PRODUCT_COUNT: Sort by organic product count.
    """

    NAME = "-name"
    MONTHLY_TREND = "-monthly_trend"
    MONTHLY_SEARCH_VOLUME_EXACT_MATCH = "-monthly_search_volume_exact"
    QUARTERLY_TREND = "-quarterly_trend"
    MONTHLY_SEARCH_VOLUME_BROAD = "-monthly_search_volume_broad"
    DOMINANT_CATEGORY = "-dominant_category"
    RECOMMENDED_PROMOTIONS = "-recommended_promotions"
    SP_BRAND_AD_BID = "-sp_brand_ad_bid"
    PPC_BID_BROAD = "-ppc_bid_broad"
    PPC_BID_EXACT = "-ppc_bid_exact"
    EASE_OF_RANKING_SCORE = "-ease_of_ranking_score"
    RELEVANCY_SCORE = "-relevancy_score"
    ORGANIC_PRODUCT_COUNT = "-organic_product_count"
