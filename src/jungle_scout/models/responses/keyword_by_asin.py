from dateutil.parser import parse

from jungle_scout.models.responses.base_response import BaseResponse


# TODO: replace with pydantic model
class KeywordByASIN(BaseResponse):
    def __init__(self, json_data):
        super().__init__(json_data)
        self.links = self._update_links(json_data)
        self.meta = self._update_meta(json_data)

    def _update_attributes(self, json_data):
        KeywordByAsinList = []
        for data in json_data["data"]:
            KeywordByAsinList.append(
                {
                    "id": data["id"],
                    "type": data["type"],
                    "attributes": {
                        "country": data["attributes"]["country"],
                        "name": data["attributes"]["name"],
                        "primary_asin": data["attributes"]["primary_asin"],
                        "monthly_trend": data["attributes"]["monthly_trend"],
                        "monthly_search_volume_exact": data["attributes"]["monthly_search_volume_exact"],
                        "quarterly_trend": data["attributes"]["quarterly_trend"],
                        "monthly_search_volume_broad": data["attributes"]["monthly_search_volume_broad"],
                        "dominant_category": data["attributes"]["dominant_category"],
                        "recommended_promotions": data["attributes"]["recommended_promotions"],
                        "sp_brand_ad_bid": data["attributes"]["sp_brand_ad_bid"],
                        "ppc_bid_broad": data["attributes"]["ppc_bid_broad"],
                        "ppc_bid_exact": data["attributes"]["ppc_bid_exact"],
                        "ease_of_ranking_score": data["attributes"]["ease_of_ranking_score"],
                        "relevancy_score": data["attributes"]["relevancy_score"],
                        "organic_product_count": data["attributes"]["organic_product_count"],
                        "sponsored_product_count": data["attributes"]["sponsored_product_count"],
                        "updated_at": parse(data["attributes"]["updated_at"]),
                        "organic_rank": data["attributes"]["organic_rank"],
                        "sponsored_rank": data["attributes"]["sponsored_rank"],
                        "overall_rank": data["attributes"]["overall_rank"],
                        "organic_ranking_asins_count": data["attributes"]["organic_ranking_asins_count"],
                        "sponsored_ranking_asins_count": data["attributes"]["sponsored_ranking_asins_count"],
                        "avg_competitor_organic_rank": data["attributes"]["avg_competitor_organic_rank"],
                        "avg_competitor_sponsored_rank": data["attributes"]["avg_competitor_sponsored_rank"],
                        "relative_organic_position": data["attributes"]["relative_organic_position"],
                        "relative_sponsored_position": data["attributes"]["relative_sponsored_position"],
                        "competitor_organic_rank": data["attributes"]["competitor_organic_rank"],
                        "variation_lowest_organic_rank": data["attributes"]["variation_lowest_organic_rank"],
                    },
                }
            )

        return KeywordByAsinList

    def _update_links(self, json_data):
        return json_data["links"]

    def _update_meta(self, json_data):
        return json_data["meta"]
