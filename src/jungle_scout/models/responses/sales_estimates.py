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
    """Represents a list of sales estimates.

    Attributes:
        - id: The ID of the sales estimate.
        - type: The type of the sales estimate.
        - asin: The ASIN (Amazon Standard Identification Number) associated with the sales estimate.
        - is_parent: A boolean indicating whether the ASIN is a parent ASIN.
        - is_variant: A boolean indicating whether the ASIN is a variant.
        - is_standalone: A boolean indicating whether the ASIN is a standalone product.
        - parent_asin: The parent ASIN associated with the sales estimate.
        - variants: The variants associated with the sales estimate.
        - data: The sales estimate data.
    """

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
