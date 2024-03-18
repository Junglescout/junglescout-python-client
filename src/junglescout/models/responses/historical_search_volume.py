from datetime import datetime

from pydantic import BaseModel, Field, field_serializer

from .serializer_helpers import serialize_date


class HistoricalSearchVolumeAttributes(BaseModel):
    """Attributes for historical search volume."""

    estimate_start_date: datetime = Field(default=..., description="The start date of the estimated search volume.")
    estimate_end_date: datetime = Field(default=..., description="The end date of the estimated search volume.")
    estimated_exact_search_volume: int = Field(default=..., description="The estimated exact search volume.")

    @field_serializer("estimate_start_date")
    def _serialize_estimate_start_date(self, v: datetime):  # noqa: PLR6301
        return serialize_date(v)

    @field_serializer("estimate_end_date")
    def _serialize_estimate_end_date(self, v: datetime):  # noqa: PLR6301
        return serialize_date(v)


class HistoricalSearchVolume(BaseModel):
    """Represents a historical search volume response."""

    id: str = Field(default=..., description="The ID of the historical search volume.")
    type: str = Field(default=..., description="The type of the historical search volume.")
    attributes: HistoricalSearchVolumeAttributes = Field(default=..., description="Attributes for the response.")
