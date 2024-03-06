from jungle_scout.base_model import BaseModel


# TODO: replace with pydantic model
class ProductDatabase(BaseModel):
    def _update_attributes(self, json_data):
        self.data_type = json_data["type"]
        self.id = json_data["id"]
