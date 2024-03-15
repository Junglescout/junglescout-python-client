from dateutil.parser import parse

from jungle_scout.models.responses.base_response import BaseResponse


# TODO: replace with pydantic model
class ProductDatabase(BaseResponse):
    """Represents a response from the product database API.

    Attributes:
        - links: The links for the response.
        - meta: The metadata for the response.
        - attributes: The attributes of the product, including:
            id: The ID of the product.
            type: The type of the product.
            title: The title of the product.
            price: The price of the product.
            reviews: The number of reviews for the product.
            category: The category of the product.
            rating: The rating of the product.
            image_url: The image URL of the product.
            parent_asin: The parent ASIN of the product.
            is_variant: Whether the product is a variant.
            seller_type: The type of the seller.
            variants: The variants of the product.
            is_standalone: Whether the product is standalone.
            is_parent: Whether the product is a parent.
            brand: The brand of the product.
            product_rank: The rank of the product.
            weight_value: The weight value of the product.
            weight_unit: The weight unit of the product.
            length_value: The length value of the product.
            width_value: The width value of the product.
            height_value: The height value of the product.
            dimensions_unit: The dimensions unit of the product.
            listing_quality_score: The listing quality score of the product.
            number_of_sellers: The number of sellers for the product.
            buy_box_owner: The buy box owner of the product.
            buy_box_owner_seller_id: The buy box owner seller ID of the product.
            date_first_available: The date the product was first available.
            date_first_available_is_estimated: Whether the date the product was first available is estimated.
            approximate_30_day_revenue: The approximate 30 day revenue of the product.
            approximate_30_day_units_sold: The approximate 30 day units sold of the product.
            ean_list: The EAN list of the product.
            variant_reviews: The variant reviews of the product.
            updated_at: The date the product was last updated.
            subcategory_ranks: The subcategory ranks of the product.
            fee_breakdown: The fee breakdown of the product.
    """

    def __init__(self, json_data):
        """Initialize the ProductDatabase.

        Args:
            json_data: The raw JSON data received from the API.
        """
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
    """Represents a response object containing subcategory ranks."""

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
    """Represents a response object containing fee breakdown."""

    def _update_attributes(self, json_data):

        return {
            "fba_fee": json_data["fba_fee"],
            "referral_fee": json_data["referral_fee"],
            "variable_closing_fee": json_data["variable_closing_fee"],
            "total_fees": json_data["total_fees"],
        }
