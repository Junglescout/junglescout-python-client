from jungle_scout.base_model import BaseModel


# TODO: replace with pydantic model
class KeywordByKeyword(BaseModel):
    def _update_attributes(self, json_data):
        self.data_type = json_data["type"]
        self.id = json_data["id"]
        self.country = json_data["attributes"]["country"]
        self.name = json_data["attributes"]["name"]
        self.monthly_trend = json_data["attributes"]["monthly_trend"]
        self.monthly_search_volume_exact = json_data["attributes"]["monthly_search_volume_exact"]
        self.quarterly_trend = json_data["attributes"]["quarterly_trend"]
        self.monthly_search_volume_broad = json_data["attributes"]["monthly_search_volume_broad"]
        self.dominant_category = json_data["attributes"]["dominant_category"]
        self.recommended_promotions = json_data["attributes"]["recommended_promotions"]
        self.sp_brand_ad_bid = json_data["attributes"]["sp_brand_ad_bid"]
        self.ppc_bid_broad = json_data["attributes"]["ppc_bid_broad"]
        self.ppc_bid_exact = json_data["attributes"]["ppc_bid_exact"]
        self.ease_of_ranking_score = json_data["attributes"]["ease_of_ranking_score"]
        self.relevancy_score = json_data["attributes"]["relevancy_score"]
        self.organic_product_count = json_data["attributes"]["organic_product_count"]
        self.sponsored_product_count = json_data["attributes"]["sponsored_product_count"]
