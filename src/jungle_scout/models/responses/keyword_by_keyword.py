from jungle_scout.models.responses.base_response import BaseResponse

# TODO: replace with pydantic model


class KeywordByKeyword(BaseResponse):
    def _update_attributes(self, json_data):
        KeywordList = []
        for data in json_data["data"]:
            KeywordList.append(
                {
                    "id": data["id"],
                    "type": data["type"],
                    "attributes": {
                        "country": data["attributes"]["country"],
                        "name": data["attributes"]["name"],
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
                    },
                }
            )

        return KeywordList

    def _update_links(self, json_data):
        return json_data["links"]

    def _update_meta(self, json_data):
        return json_data["meta"]
