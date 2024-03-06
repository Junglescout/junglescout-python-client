from dateutil.parser import parse

from jungle_scout.base_model import BaseModel


class ShareOfVoice(BaseModel):
    def _update_attributes(self, json_data):
        self.type = json_data["type"]
        self.id = json_data["id"]
        self.estimated_30_day_search_volume = json_data["attributes"]["estimated_30_day_search_volume"]
        self.exact_suggested_bid_median = json_data["attributes"]["exact_suggested_bid_median"]
        self.product_count = json_data["attributes"]["product_count"]
        self.updated_at = parse(json_data["attributes"]["updated_at"])
        self.brands = [ShareOfVoiceBrands(each) for each in json_data["attributes"]["brands"]]
        self.top_asins = [ShareOfVoiceTopAsins(each) for each in json_data["attributes"]["top_asins"]]
        self.top_asins_model_start_date = parse(json_data["attributes"]["top_asins_model_start_date"])
        self.top_asins_model_end_date = parse(json_data["attributes"]["top_asins_model_end_date"])


class ShareOfVoiceBrands(BaseModel):
    def _update_attributes(self, json_data):
        self.brand = json_data["brand"]
        self.combined_products = json_data["combined_products"]
        self.combined_weighted_sov = json_data["combined_weighted_sov"]
        self.combined_basic_sov = json_data["combined_basic_sov"]
        self.combined_average_position = json_data["combined_average_position"]
        self.combined_average_price = json_data["combined_average_price"]
        self.organic_products = json_data["organic_products"]
        self.organic_weighted_sov = json_data["organic_weighted_sov"]
        self.organic_basic_sov = json_data["organic_basic_sov"]
        self.organic_average_position = json_data["organic_average_position"]
        self.organic_average_price = json_data["organic_average_price"]
        self.sponsored_products = json_data["sponsored_products"]
        self.sponsored_weighted_sov = json_data["sponsored_weighted_sov"]
        self.sponsored_basic_sov = json_data["sponsored_basic_sov"]
        self.sponsored_average_position = json_data["sponsored_average_position"]
        self.sponsored_average_price = json_data["sponsored_average_price"]


class ShareOfVoiceTopAsins(BaseModel):
    def _update_attributes(self, json_data):
        print(json_data)
        self.asin = json_data["asin"]
        self.name = json_data["name"]
        self.brand = json_data["brand"]
        self.clicks = json_data["clicks"]
        self.conversions = json_data["conversions"]
        self.conversion_rate = json_data["conversion_rate"]
