from jungle_scout.base_model import BaseModel


class SalesEstimateData(BaseModel):
    def _update_attributes(self, json_data):
        self.date = json_data["date"]
        self.estimated_units_sold = json_data["estimated_units_sold"]
        self.last_known_price = json_data["last_known_price"]


class SalesEstimates(BaseModel):
    def _update_attributes(self, json_data):
        self.id = json_data["id"]
        self.data_type = json_data["type"]
        self.asin = json_data["attributes"]["asin"]
        self.is_parent = json_data["attributes"]["is_parent"]
        self.is_variant = json_data["attributes"]["is_variant"]
        self.is_standalone = json_data["attributes"]["is_standalone"]
        self.parent_asin = json_data["attributes"]["parent_asin"]
        self.variants = json_data["attributes"]["variants"]
        self.data = [SalesEstimateData(each) for each in json_data["attributes"]["data"]]
