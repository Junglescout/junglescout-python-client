from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, field_serializer

from .serializer_helpers import serialize_datetime


class ShareOfVoiceBrands(BaseModel):
    """Represents a list of brands in the Share of Voice response."""

    brand: Optional[str] = Field(default=None, description="The name of the brand.")
    combined_products: Optional[int] = Field(default=None, description="The count of combined products.")
    combined_weighted_sov: Optional[float] = Field(default=None, description="The combined weighted share of voice.")
    combined_basic_sov: Optional[float] = Field(default=None, description="The combined basic share of voice.")
    combined_average_position: Optional[float] = Field(default=None, description="The combined average position.")
    combined_average_price: Optional[float] = Field(default=None, description="The combined average price.")
    organic_products: Optional[int] = Field(default=None, description="The organic products.")
    organic_weighted_sov: Optional[float] = Field(default=None, description="The organic weighted share of voice.")
    organic_basic_sov: Optional[float] = Field(default=None, description="The organic basic share of voice.")
    organic_average_position: Optional[float] = Field(default=None, description="The organic average position.")
    organic_average_price: Optional[float] = Field(default=None, description="The organic average price.")
    sponsored_products: Optional[int] = Field(default=None, description="The sponsored products.")
    sponsored_weighted_sov: Optional[float] = Field(default=None, description="The sponsored weighted share of voice.")
    sponsored_basic_sov: Optional[float] = Field(default=None, description="The sponsored basic share of voice.")
    sponsored_average_position: Optional[float] = Field(default=None, description="The sponsored average position.")
    sponsored_average_price: Optional[float] = Field(default=None, description="The sponsored average price.")


class ShareOfVoiceTopAsins(BaseModel):
    """Represents a list of top ASINs in the Share of Voice response."""

    asin: Optional[str] = Field(default=None, description="The ASIN.")
    name: Optional[str] = Field(default=None, description="The name.")
    brand: Optional[str] = Field(default=None, description="The brand.")
    clicks: Optional[int] = Field(default=None, description="The clicks.")
    conversions: Optional[int] = Field(default=None, description="The conversions.")
    conversion_rate: Optional[float] = Field(default=None, description="The conversion rate.")


class ShareOfVoiceAttributes(BaseModel):
    """Attributes for the Share of Voice response."""

    estimated_30_day_search_volume: int = Field(default=..., description="The estimated 30-day search volume.")
    exact_suggested_bid_median: Optional[float] = Field(
        default=None, description="The median of the exact suggested bid."
    )
    product_count: int = Field(default=..., description="The count of products.")
    updated_at: datetime = Field(
        default=..., description="The date and time when the Share of Voice data was last updated."
    )
    brands: List[ShareOfVoiceBrands] = Field(
        default=..., description="The brands associated with the Share of Voice data."
    )
    top_asins: List[ShareOfVoiceTopAsins] = Field(
        default=..., description="The top ASINs associated with the Share of Voice data."
    )
    top_asins_model_start_date: datetime = Field(default=..., description="The start date of the top ASINs model.")
    top_asins_model_end_date: datetime = Field(default=..., description="The end date of the top ASINs model.")

    @field_serializer("top_asins_model_start_date")
    def _serialize_top_asins_model_start_date(self, v: datetime):  # noqa: PLR6301
        return serialize_datetime(v)

    @field_serializer("top_asins_model_end_date")
    def _serialize_top_asins_model_end_date(self, v: datetime):  # noqa: PLR6301
        return serialize_datetime(v)

    @field_serializer("updated_at")
    def _serialize_updated_at(self, v: datetime):  # noqa: PLR6301
        return serialize_datetime(v)


class ShareOfVoice(BaseModel):
    """Represents the Share of Voice response from the Jungle Scout API."""

    type: str = Field(default=..., description="The type of the Share of Voice response.")
    id: str = Field(default=..., description="The ID of the Share of Voice response.")
    attributes: ShareOfVoiceAttributes = Field(
        default=..., description="The attributes of the Share of Voice response."
    )
