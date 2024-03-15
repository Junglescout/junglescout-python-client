from dateutil.parser import parse

from jungle_scout.models.responses.base_response import BaseResponse


# TODO: replace with pydantic model
class KeywordByASIN(BaseResponse):
    """Represents a response object containing keyword data for a specific ASIN.

    Attributes:
        - links: The links for the response.
        - meta: The metadata for the response.
        - attributes: The attributes of the keyword, including:
            - country: The country of the keyword.
            - name: The name of the keyword.
            - primary_asin: The primary ASIN of the keyword.
            - monthly_trend: The monthly trend of the keyword.
            - monthly_search_volume_exact: The monthly search volume exact of the keyword.
            - quarterly_trend: The quarterly trend of the keyword.
            - monthly_search_volume_broad: The monthly search volume broad of the keyword.
            - dominant_category: The dominant category of the keyword.
            - recommended_promotions: The recommended promotions of the keyword.
            - sp_brand_ad_bid: The SP brand ad bid of the keyword.
            - ppc_bid_broad: The PPC bid broad of the keyword.
            - ppc_bid_exact: The PPC bid exact of the keyword.
            - ease_of_ranking_score: The ease of ranking score of the keyword.
            - relevancy_score: The relevancy score of the keyword.
            - organic_product_count: The organic product count of the keyword.
            - sponsored_product_count: The sponsored product count of the keyword.
            - updated_at: The date the keyword was last updated.
            - organic_rank: The organic rank of the keyword.
            - sponsored_rank: The sponsored rank of the keyword.
            - overall_rank: The overall rank of the keyword.
            - organic_ranking_asins_count: The organic ranking ASINs count of the keyword.
            - sponsored_ranking_asins_count: The sponsored ranking ASINs count of the keyword.
            - avg_competitor_organic_rank: The average competitor organic rank of the keyword.
            - avg_competitor_sponsored_rank: The average competitor sponsored rank of the keyword.
            - relative_organic_position: The relative organic position of the keyword.
            - relative_sponsored_position: The relative sponsored position of the keyword.
            - competitor_organic_rank: The competitor organic rank of the keyword.
            - variation_lowest_organic_rank: The variation lowest organic rank of the keyword.
    """

    def __init__(self, json_data):
        """Initialize the KeywordByASIN.

        Args:
            json_data: The raw JSON data received from the API.
        """
        super().__init__(json_data)
        self.links = self._update_links(json_data)
        self.meta = self._update_meta(json_data)

    def _update_attributes(self, json_data):
        keyword_by_asin_list = []
        for data in json_data["data"]:
            keyword_by_asin_list.append(
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

        return keyword_by_asin_list

    def _update_links(self, json_data):
        return json_data["links"]

    def _update_meta(self, json_data):
        return json_data["meta"]
