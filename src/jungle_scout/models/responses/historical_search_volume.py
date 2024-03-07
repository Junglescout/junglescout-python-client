from jungle_scout.models.responses.base_response import BaseResponse


# TODO: replace with pydantic model
class HistoricalSearchVolume(BaseResponse):
    def _update_attributes(self, json_data):
        HistoricalSearchVolumeList = []

        for data in json_data["data"]:
            HistoricalSearchVolumeList.append(
                {
                    "id": data["id"],
                    "type": data["type"],
                    "attributes": {
                        "estimate_start_date": data["attributes"]["estimate_start_date"],
                        "estimate_end_date": data["attributes"]["estimate_end_date"],
                        "estimated_exact_search_volume": data["attributes"]["estimated_exact_search_volume"],
                    },
                }
            )

        return HistoricalSearchVolumeList
