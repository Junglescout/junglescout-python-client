from jungle_scout.models.responses.base_response import BaseResponse


# TODO: replace with pydantic model
class HistoricalSearchVolume(BaseResponse):
    def _update_attributes(self, json_data):
        self.data_type = json_data["type"]
        self.id = json_data["id"]
        self.estimate_start_date = json_data["attributes"]["estimate_start_date"]
        self.estimate_end_date = json_data["attributes"]["estimate_end_date"]
        self.estimated_exact_search_volume = json_data["attributes"]["estimated_exact_search_volume"]
