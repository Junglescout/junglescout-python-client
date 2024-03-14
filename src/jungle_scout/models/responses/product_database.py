from dateutil.parser import parse

from jungle_scout.models.responses.base_response import BaseResponse


# TODO: replace with pydantic model
class ProductDatabase(BaseResponse):
    """Represents a response from the product database API.

    Attributes:
        links (dict): A dictionary containing links related to the response.
        meta (dict): A dictionary containing metadata related to the response.
    """

    def __init__(self, json_data):
        super().__init__(json_data)
        self.links = self._update_links(json_data)
        self.meta = self._update_meta(json_data)

    def _update_attributes(self, json_data):

        productDatabaseList = []

        for data in json_data["data"]:
            dictItem = {
                "id": data["id"],
                "type": data["type"],
                "attributes": {
                    "title": data["attributes"]["title"],
                    "price": data["attributes"]["price"],
                    "reviews": data["attributes"]["reviews"],
                    "category": data["attributes"]["category"],
                    "rating": data["attributes"]["rating"],
                    "image_url": data["attributes"]["image_url"],
                    "parent_asin": data["attributes"]["parent_asin"],
                    "is_variant": data["attributes"]["is_variant"],
                    "seller_type": data["attributes"]["seller_type"],
                    "variants": data["attributes"]["variants"],
                    "is_standalone": data["attributes"]["is_standalone"],
                    "is_parent": data["attributes"]["is_parent"],
                    "brand": data["attributes"]["brand"],
                    "product_rank": data["attributes"]["product_rank"],
                    "weight_value": data["attributes"]["weight_value"],
                    "weight_unit": data["attributes"]["weight_unit"],
                    "length_value": data["attributes"]["length_value"],
                    "width_value": data["attributes"]["width_value"],
                    "height_value": data["attributes"]["height_value"],
                    "dimensions_unit": data["attributes"]["dimensions_unit"],
                    "listing_quality_score": data["attributes"]["listing_quality_score"],
                    "number_of_sellers": data["attributes"]["number_of_sellers"],
                    "buy_box_owner": data["attributes"]["buy_box_owner"],
                    "buy_box_owner_seller_id": data["attributes"]["buy_box_owner_seller_id"],
                    "date_first_available": data["attributes"]["date_first_available"],
                    "date_first_available_is_estimated": data["attributes"]["date_first_available_is_estimated"],
                    "approximate_30_day_revenue": data["attributes"]["approximate_30_day_revenue"],
                    "approximate_30_day_units_sold": data["attributes"]["approximate_30_day_units_sold"],
                    "ean_list": data["attributes"]["ean_list"],
                    "variant_reviews": data["attributes"]["variant_reviews"],
                    "updated_at": parse(data["attributes"]["updated_at"]),
                },
            }

            subcategory_ranks_data = data["attributes"]["subcategory_ranks"]
            if subcategory_ranks_data is not None:
                dictItem["attributes"].update({"subcategory_ranks": SubcategoryRanks(subcategory_ranks_data).data})

            fee_breakdown_data = data["attributes"]["fee_breakdown"]
            if fee_breakdown_data is not None:
                dictItem["attributes"].update({"fee_breakdown": FeeBreakdown(fee_breakdown_data).data})

            productDatabaseList.append(dictItem)

        return productDatabaseList

    def _update_links(self, json_data):
        return json_data["links"]

    def _update_meta(self, json_data):
        return json_data["meta"]


class SubcategoryRanks(BaseResponse):
    def _update_attributes(self, json_data):
        subcategoryRanksList = []

        for data in json_data:
            subcategoryRanksList.append(
                {
                    "subcategory": data["subcategory"],
                    "rank": data["rank"],
                }
            )

        return subcategoryRanksList


class FeeBreakdown(BaseResponse):
    def _update_attributes(self, json_data):

        return {
            "fba_fee": json_data["fba_fee"],
            "referral_fee": json_data["referral_fee"],
            "variable_closing_fee": json_data["variable_closing_fee"],
            "total_fees": json_data["total_fees"],
        }
