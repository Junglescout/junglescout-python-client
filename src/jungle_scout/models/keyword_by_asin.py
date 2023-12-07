from dateutil.parser import parse

from jungle_scout.base_model import BaseModel


class KeywordByASIN(BaseModel):
    def _update_attributes(self, data):
        self.data_type = data["type"]
        self.id = data["id"]
        self.country = data["attributes"]["country"]
        self.name = data["attributes"]["name"]
        self.primary_asin = data["attributes"]["primary_asin"]
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
        self.updated_at = parse(data["attributes"]["updated_at"])
        self.organic_rank = data["attributes"]["organic_rank"]
        self.sponsored_rank = data["attributes"]["sponsored_rank"]
        self.overall_rank = data["attributes"]["overall_rank"]
        self.organic_ranking_asins_count = data["attributes"]["organic_ranking_asins_count"]
        self.sponsored_ranking_asins_count = data["attributes"]["sponsored_ranking_asins_count"]
        self.avg_competitor_organic_rank = data["attributes"]["avg_competitor_organic_rank"]
        self.avg_competitor_sponsored_rank = data["attributes"]["avg_competitor_sponsored_rank"]
        self.relative_organic_position = data["attributes"]["relative_organic_position"]
        self.relative_sponsored_position = data["attributes"]["relative_sponsored_position"]
        self.competitor_organic_rank = data["attributes"]["competitor_organic_rank"]
        self.variation_lowest_organic_rank = data["attributes"]["variation_lowest_organic_rank"]
