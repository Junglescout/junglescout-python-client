from jungle_scout.models.responses.base_response import BaseResponse


class SalesEstimateData(BaseResponse):
    def _update_attributes(self, json_data):
        SalesEstimateDataList = []

        for data in json_data["data"]:
            SalesEstimateDataList.append(
                {
                    "date": data["date"],
                    "estimated_units_sold": data["estimated_units_sold"],
                    "last_known_price": data["last_known_price"],
                }
            )
        return SalesEstimateDataList


class SalesEstimates(BaseResponse):
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
                        "data": SalesEstimateData(data["attributes"]).data,
                    },
                }
            )
        return SalesEstimateList
