from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from junglescout.models.parameters.marketplace import Marketplace
from junglescout.models.parameters.sort import Sort


class Params(BaseModel):
    """Represents the parameters for a request to the Jungle Scout API."""

    marketplace: Marketplace = Field(default=..., description="The marketplace to query.")
    sort: Optional[Sort] = Field(
        default=None, description="The sorting option for the results. Must be a valid Sort object."
    )
    page: Optional[str] = Field(
        default=None, serialization_alias="page[cursor]", description="The cursor for pagination."
    )
    page_size: Optional[int] = Field(
        default=50, serialization_alias="page[size]", description="The number of results per page."
    )

    @field_serializer("marketplace")
    def _serialize_marketplace(self, value: Marketplace):  # noqa: PLR6301
        return value.country_code

    @field_serializer("sort")
    def _serialize_sort(self, value: Optional[Sort]):  # noqa: PLR6301
        return value.value if value else None
