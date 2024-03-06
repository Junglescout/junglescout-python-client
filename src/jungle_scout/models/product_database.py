from dateutil.parser import parse

from jungle_scout.base_model import BaseModel


# TODO: replace with pydantic model
class ProductDatabase(BaseModel):
    def _update_attributes(self, json_data):
        self.data_type = json_data["type"]
        self.id = json_data["id"]
        self.title = json_data["attributes"]["title"]
        self.price = json_data["attributes"]["price"]
        self.reviews = json_data["attributes"]["reviews"]
        self.category = json_data["attributes"]["category"]
        self.rating = json_data["attributes"]["rating"]
        self.image_url = json_data["attributes"]["image_url"]
        self.parent_asin = json_data["attributes"]["parent_asin"]
        self.is_variant = json_data["attributes"]["is_variant"]
        self.seller_type = json_data["attributes"]["seller_type"]
        self.variants = json_data["attributes"]["variants"]
        self.is_standalone = json_data["attributes"]["is_standalone"]
        self.is_parent = json_data["attributes"]["is_parent"]
        self.brand = json_data["attributes"]["brand"]
        self.product_rank = json_data["attributes"]["product_rank"]
        self.weight_value = json_data["attributes"]["weight_value"]
        self.weight_unit = json_data["attributes"]["weight_unit"]
        self.length_value = json_data["attributes"]["length_value"]
        self.width_value = json_data["attributes"]["width_value"]
        self.height_value = json_data["attributes"]["height_value"]
        self.dimensions_unit = json_data["attributes"]["dimensions_unit"]
        self.listing_quality_score = json_data["attributes"]["listing_quality_score"]
        self.number_of_sellers = json_data["attributes"]["number_of_sellers"]
        self.buy_box_owner = json_data["attributes"]["buy_box_owner"]
        self.buy_box_owner_seller_id = json_data["attributes"]["buy_box_owner_seller_id"]
        self.date_first_available = json_data["attributes"]["date_first_available"]
        self.date_first_available_is_estimated = json_data["attributes"]["date_first_available_is_estimated"]
        self.approximate_30_day_revenue = json_data["attributes"]["approximate_30_day_revenue"]
        self.approximate_30_day_units_sold = json_data["attributes"]["approximate_30_day_units_sold"]
        self.ean_list = json_data["attributes"]["ean_list"]
        self.variant_reviews = json_data["attributes"]["variant_reviews"]
        self.updated_at = parse(json_data["attributes"]["updated_at"])

        subcategory_ranks_data = json_data["attributes"].get("subcategory_ranks")
        if subcategory_ranks_data is not None:
            self.subcategory_ranks = [SubcategoryRanks(each) for each in subcategory_ranks_data]

        fee_breakdown_data = json_data["attributes"].get("fee_breakdown")
        if fee_breakdown_data is not None:
            self.fee_breakdown = FeeBreakdown(fee_breakdown_data)


class SubcategoryRanks(BaseModel):
    def _update_attributes(self, json_data):
        self.subcategory = json_data["subcategory"]
        self.rank = json_data["rank"]


class FeeBreakdown(BaseModel):
    def _update_attributes(self, json_data):
        self.fba_fee = json_data["fba_fee"]
        self.referral_fee = json_data["referral_fee"]
        self.variable_closing_fee = json_data["variable_closing_fee"]
        self.total_fees = json_data["total_fees"]
