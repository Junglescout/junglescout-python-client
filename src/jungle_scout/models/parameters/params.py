from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.sort import Sort


class Params(BaseModel):
    marketplace: Marketplace
    sort: Optional[Sort] = None
    page: Optional[str] = Field(None, serialization_alias="page[cursor]")
    page_size: int = Field(50, serialization_alias="page[size]")

    @field_serializer("marketplace")
    def serialize_marketplace(self, value: Marketplace):
        return value.country_code

    @field_serializer("sort")
    def serialize_sort(self, value: Optional[Sort]):
        return value.value if value else None
