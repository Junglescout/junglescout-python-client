from jungle_scout.base_model import BaseModel


class SalesEstimateData(BaseModel):
    def _update_attributes(self, data):
        self.date = data["date"]
        self.estimated_units_sold = data["estimated_units_sold"]
        self.last_known_price = data["last_known_price"]


class SalesEstimates(BaseModel):
    def _update_attributes(self, data):
        self.id = data["id"]
        self.type = data["type"]
        self.asin = data["attributes"]["asin"]
        self.is_parent = data["attributes"]["is_parent"]
        self.is_variant = data["attributes"]["is_variant"]
        self.is_standalone = data["attributes"]["is_standalone"]
        self.parent_asin = data["attributes"]["parent_asin"]
        self.variants = data["attributes"]["variants"]
        self.data = [SalesEstimateData(each) for each in data["attributes"]["data"]]
