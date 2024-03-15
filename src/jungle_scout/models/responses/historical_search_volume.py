from jungle_scout.models.responses.base_response import BaseResponse


# TODO: replace with pydantic model
class HistoricalSearchVolume(BaseResponse):
    """Represents a historical search volume response.

    Attributes:
        - id: The ID of the historical search volume.
        - type: The type of the historical search volume.
        - attributes: The attributes of the historical search volume, including:
            - estimate_start_date: The start date of the estimated search volume.
            - estimate_end_date: The end date of the estimated search volume.
            - estimated_exact_search_volume: The estimated exact search volume.
    """

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
