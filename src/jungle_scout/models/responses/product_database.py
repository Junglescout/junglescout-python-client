from jungle_scout.models.responses.base_response import BaseResponse


# TODO: replace with pydantic model
class ProductDatabase(BaseResponse):
    """
    Represents a response from the product database API.

    Attributes:
        links (dict): A dictionary containing links related to the response.
        meta (dict): A dictionary containing metadata related to the response.
    """

    def __init__(self, json_data):
        super().__init__(json_data)
        self.links = self._update_links(json_data)
        self.meta = self._update_meta(json_data)

    def _update_attributes(self, json_data):
        productDatabaseList = []

        for data in json_data["data"]:
            dictItem = {
                # Attribute mappings...
            }

            # Update subcategory ranks if available
            subcategory_ranks_data = data["attributes"]["subcategory_ranks"]
            if subcategory_ranks_data is not None:
                dictItem["attributes"].update({"subcategory_ranks": SubcategoryRanks(subcategory_ranks_data).data})

            fee_breakdown_data = data["attributes"]["fee_breakdown"]
            if fee_breakdown_data is not None:
                dictItem["attributes"].update({"fee_breakdown": FeeBreakdown(fee_breakdown_data).data})

            productDatabaseList.append(dictItem)

        return productDatabaseList

    def _update_links(self, json_data):
        return json_data["links"]

    def _update_meta(self, json_data):
        return json_data["meta"]


class SubcategoryRanks(BaseResponse):
    def _update_attributes(self, json_data):
        subcategoryRanksList = []

        for data in json_data:
            subcategoryRanksList.append(
                {
                    "subcategory": data["subcategory"],
                    "rank": data["rank"],
                }
            )

        return subcategoryRanksList


class FeeBreakdown(BaseResponse):
    def _update_attributes(self, json_data):

        return {
            "fba_fee": json_data["fba_fee"],
            "referral_fee": json_data["referral_fee"],
            "variable_closing_fee": json_data["variable_closing_fee"],
            "total_fees": json_data["total_fees"],
        }
