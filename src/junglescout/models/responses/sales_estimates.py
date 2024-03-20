from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, field_serializer

from .serializer_helpers import serialize_date


class SalesEstimateData(BaseModel):
    """Represents sales estimates data."""

    date: datetime = Field(default=..., description="The date of the sales estimate.")
    estimated_units_sold: int = Field(default=..., description="The estimated units sold.")
    last_known_price: float = Field(default=..., description="The last known price.")

    @field_serializer("date")
    def _serialize_date(self, v: datetime):  # noqa: PLR6301
        return serialize_date(v)


class SalesEstimateAttributes(BaseModel):
    """The attributes of the sales estimate."""

    asin: str = Field(
        default=..., description="The ASIN (Amazon Standard Identification Number) associated with the sales estimate."
    )
    is_parent: bool = Field(default=..., description="A boolean indicating whether the ASIN is a parent ASIN.")
    is_variant: bool = Field(default=..., description="A boolean indicating whether the ASIN is a variant.")
    is_standalone: bool = Field(
        default=..., description="A boolean indicating whether the ASIN is a standalone product."
    )
    parent_asin: str = Field(default=..., description="The parent ASIN associated with the sales estimate.")
    variants: List[str] = Field(default=..., description="The variant ASINs associated with the sales estimate.")
    data: List[SalesEstimateData] = Field(default=..., description="The sales estimate data.")


class SalesEstimates(BaseModel):
    """Represents a list of sales estimates."""

    id: str = Field(default=..., description="The ID of the sales estimate.")
    type: str = Field(default=..., description="The type of the sales estimate.")
    attributes: SalesEstimateAttributes = Field(default=..., description="The attributes of the sales estimate.")
