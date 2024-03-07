from dateutil.parser import parse

from jungle_scout.models.responses.base_response import BaseResponse


# TODO: replace with pydantic model
class KeywordByASIN(BaseResponse):
    def _update_attributes(self, json_data):
        self.data_type = json_data["type"]
        self.id = json_data["id"]
        self.country = json_data["attributes"]["country"]
        self.name = json_data["attributes"]["name"]
        self.primary_asin = json_data["attributes"]["primary_asin"]
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
        self.updated_at = parse(json_data["attributes"]["updated_at"])
        self.organic_rank = json_data["attributes"]["organic_rank"]
        self.sponsored_rank = json_data["attributes"]["sponsored_rank"]
        self.overall_rank = json_data["attributes"]["overall_rank"]
        self.organic_ranking_asins_count = json_data["attributes"]["organic_ranking_asins_count"]
        self.sponsored_ranking_asins_count = json_data["attributes"]["sponsored_ranking_asins_count"]
        self.avg_competitor_organic_rank = json_data["attributes"]["avg_competitor_organic_rank"]
        self.avg_competitor_sponsored_rank = json_data["attributes"]["avg_competitor_sponsored_rank"]
        self.relative_organic_position = json_data["attributes"]["relative_organic_position"]
        self.relative_sponsored_position = json_data["attributes"]["relative_sponsored_position"]
        self.competitor_organic_rank = json_data["attributes"]["competitor_organic_rank"]
        self.variation_lowest_organic_rank = json_data["attributes"]["variation_lowest_organic_rank"]

    def _update_links(self, json_data):
        pass

    def _update_meta(self, json_data):
        pass
