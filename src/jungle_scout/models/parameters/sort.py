from enum import Enum


class Sort(Enum):
    name = "-name"
    monthly_trend = "-monthly_trend"
    monthly_search_volume_exact = "-monthly_search_volume_exact"
    quarterly_trend = "-quarterly_trend"
    monthly_search_volume_broad = "-monthly_search_volume_broad"
    dominant_category = "-dominant_category"
    recommended_promotions = "-recommended_promotions"
    sp_brand_ad_bid = "-sp_brand_ad_bid"
    ppc_bid_broad = "-ppc_bid_broad"
    ppc_bid_exact = "-ppc_bid_exact"
    ease_of_ranking_score = "-ease_of_ranking_score"
    relevancy_score = "-relevancy_score"
    organic_product_count = "-organic_product_count"
