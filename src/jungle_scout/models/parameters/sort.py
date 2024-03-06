from enum import Enum


class Sort(Enum):
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
