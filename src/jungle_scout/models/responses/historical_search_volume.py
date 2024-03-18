from datetime import datetime

from pydantic import BaseModel, Field


class HistoricalSearchVolumeAttributes(BaseModel):
    """Attributes for historical search volume."""

    estimate_start_date: datetime = Field(default=..., description="The start date of the estimated search volume.")
    estimate_end_date: datetime = Field(default=..., description="The end date of the estimated search volume.")
    estimated_exact_search_volume: int = Field(default=..., description="The estimated exact search volume.")


class HistoricalSearchVolume(BaseModel):
    """Represents a historical search volume response."""

    id: str = Field(default=..., description="The ID of the historical search volume.")
    type: str = Field(default=..., description="The type of the historical search volume.")
    attributes: HistoricalSearchVolumeAttributes = Field(default=..., description="Attributes for the response.")
