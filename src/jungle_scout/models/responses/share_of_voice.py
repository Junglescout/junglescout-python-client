from dateutil.parser import parse

from jungle_scout.models.responses.base_response import BaseResponse


class ShareOfVoice(BaseResponse):
    """Represents the Share of Voice response from the Jungle Scout API.

    Attributes:
        - type: The type of the Share of Voice response.
        - id: The ID of the Share of Voice response.
        - attributes: The attributes of the Share of Voice response, including:
            estimated_30_day_search_volume: The estimated 30-day search volume.
            exact_suggested_bid_median: The median of the exact suggested bid.
            product_count: The count of products.
            updated_at: The date and time when the Share of Voice data was last updated.
            brands: The brands associated with the Share of Voice data.
            top_asins: The top ASINs associated with the Share of Voice data.
            top_asins_model_start_date: The start date of the top ASINs model.
            top_asins_model_end_date: The end date of the top ASINs model.
    """

    def _update_attributes(self, json_data):
        return [
            {
                "type": json_data["type"],
                "id": json_data["id"],
                "attributes": {
                    "estimated_30_day_search_volume": json_data["attributes"]["estimated_30_day_search_volume"],
                    "exact_suggested_bid_median": json_data["attributes"]["exact_suggested_bid_median"],
                    "product_count": json_data["attributes"]["product_count"],
                    "updated_at": parse(json_data["attributes"]["updated_at"]),
                    "brands": ShareOfVoiceBrands(json_data["attributes"]).data,
                    "top_asins": ShareOfVoiceTopAsins(json_data["attributes"]).data,
                    "top_asins_model_start_date": parse(json_data["attributes"]["top_asins_model_start_date"]),
                    "top_asins_model_end_date": parse(json_data["attributes"]["top_asins_model_end_date"]),
                },
            }
        ]


class ShareOfVoiceBrands(BaseResponse):
    """Represents a list of brands in the Share of Voice response."""

    def _update_attributes(self, json_data):
        ShareOfVoiceBrandsList = []

        for data in json_data["brands"]:
            ShareOfVoiceBrandsList.append(
                {
                    "brand": data["brand"],
                    "combined_products": data["combined_products"],
                    "combined_weighted_sov": data["combined_weighted_sov"],
                    "combined_basic_sov": data["combined_basic_sov"],
                    "combined_average_position": data["combined_average_position"],
                    "combined_average_price": data["combined_average_price"],
                    "organic_products": data["organic_products"],
                    "organic_weighted_sov": data["organic_weighted_sov"],
                    "organic_basic_sov": data["organic_basic_sov"],
                    "organic_average_position": data["organic_average_position"],
                    "organic_average_price": data["organic_average_price"],
                    "sponsored_products": data["sponsored_products"],
                    "sponsored_weighted_sov": data["sponsored_weighted_sov"],
                    "sponsored_basic_sov": data["sponsored_basic_sov"],
                    "sponsored_average_position": data["sponsored_average_position"],
                    "sponsored_average_price": data["sponsored_average_price"],
                }
            )

        return ShareOfVoiceBrandsList


class ShareOfVoiceTopAsins(BaseResponse):
    """Represents a list of top ASINs in the Share of Voice response."""

    def _update_attributes(self, json_data):
        ShareOfVoiceTopAsinsList = []
        for data in json_data["top_asins"]:
            ShareOfVoiceTopAsinsList.append(
                {
                    "asin": data["asin"],
                    "name": data["name"],
                    "brand": data["brand"],
                    "clicks": data["clicks"],
                    "conversions": data["conversions"],
                    "conversion_rate": data["conversion_rate"],
                }
            )

        return ShareOfVoiceTopAsinsList
