from jungle_scout.base_model import BaseModel


# TODO: replace with pydantic model
class HistoricalSearchVolume(BaseModel):
    def _update_attributes(self, data):
        self.data_type = data["type"]
        self.id = data["id"]
        self.estimate_start_date = data["attributes"]["estimate_start_date"]
        self.estimate_end_date = data["attributes"]["estimate_end_date"]
        self.estimated_exact_search_volume = data["attributes"]["estimated_exact_search_volume"]
