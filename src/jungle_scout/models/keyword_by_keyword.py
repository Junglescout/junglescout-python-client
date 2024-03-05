from dateutil.parser import parse

from jungle_scout.base_model import BaseModel


class KeywordByKeyword(BaseModel):
    def _update_attributes(self, data):
        self.data_type = data["type"]
        self.id = data["id"]
        self.country = data["attributes"]["country"]
        self.name = data["attributes"]["name"]
        self.monthly_trend = data["attributes"]["monthly_trend"]
        self.monthly_search_volume_exact = data["attributes"]["monthly_search_volume_exact"]
        self.quarterly_trend = data["attributes"]["quarterly_trend"]
        self.monthly_search_volume_broad = data["attributes"]["monthly_search_volume_broad"]
        self.dominant_category = data["attributes"]["dominant_category"]
        self.recommended_promotions = data["attributes"]["recommended_promotions"]
        self.sp_brand_ad_bid = data["attributes"]["sp_brand_ad_bid"]
        self.ppc_bid_broad = data["attributes"]["ppc_bid_broad"]
        self.ppc_bid_exact = data["attributes"]["ppc_bid_exact"]
        self.ease_of_ranking_score = data["attributes"]["ease_of_ranking_score"]
        self.relevancy_score = data["attributes"]["relevancy_score"]
        self.organic_product_count = data["attributes"]["organic_product_count"]
        self.sponsored_product_count = data["attributes"]["sponsored_product_count"]
