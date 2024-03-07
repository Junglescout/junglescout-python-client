from jungle_scout.models.responses.base_response import BaseResponse


class SalesEstimateData(BaseResponse):
    def _update_attributes(self, json_data):
        self.date = json_data["date"]
        self.estimated_units_sold = json_data["estimated_units_sold"]
        self.last_known_price = json_data["last_known_price"]

    def _update_links(self, json_data):
        pass

    def _update_meta(self, json_data):
        pass


class SalesEstimates(BaseResponse):
    def _update_attributes(self, json_data):

        self.asin = json_data["attributes"]["asin"]
        self.is_parent = json_data["attributes"]["is_parent"]
        self.is_variant = json_data["attributes"]["is_variant"]
        self.is_standalone = json_data["attributes"]["is_standalone"]
        self.parent_asin = json_data["attributes"]["parent_asin"]
        self.variants = json_data["attributes"]["variants"]
        self.data = [SalesEstimateData(each) for each in json_data["attributes"]["data"]]

    def _update_attributes(self, json_data):
        SalesEstimateList = []

        for data in json_data["data"]:
            SalesEstimateList.append(
                {
                    "id": data["id"],
                    "type": data["type"],
                    "attributes": {
                        "asin": data["attributes"]["asin"],
                        "is_parent": data["attributes"]["is_parent"],
                        "is_variant": data["attributes"]["is_variant"],
                        "is_standalone": data["attributes"]["is_standalone"],
                        "parent_asin": data["attributes"]["parent_asin"],
                        "variants": data["attributes"]["variants"],
                        "data": [SalesEstimateData(each) for each in data["attributes"]["data"]],
                    },
                }
            )
        return SalesEstimateList
