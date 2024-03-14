from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.sort import Sort


class Params(BaseModel):
    """Represents the parameters for a request to the Jungle Scout API.

    Attributes:
        marketplace (Marketplace): The marketplace to query.
        sort (Optional[Sort]): The sorting option for the results. Must be a valid Sort object. Defaults to None.
        page (Optional[str]): The cursor for pagination. Defaults to None.
        page_size (Optional[int]): The number of results per page. Defaults to 50.
    """

    marketplace: Marketplace
    sort: Optional[Sort] = None
    page: Optional[str] = Field(default=None, serialization_alias="page[cursor]")
    page_size: Optional[int] = Field(default=50, serialization_alias="page[size]")

    @field_serializer("marketplace")
    def serialize_marketplace(self, value: Marketplace):
        return value.country_code

    @field_serializer("sort")
    def serialize_sort(self, value: Optional[Sort]):
        return value.value if value else None
