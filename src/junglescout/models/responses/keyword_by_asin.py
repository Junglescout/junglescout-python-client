from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, field_serializer

from .serializer_helpers import serialize_datetime


class CompetitorRank(BaseModel):
    """Represents a competitor's rank for a specific keyword."""

    asin: str = Field(default=..., description="The ASIN of the competitor.")
    organic_rank: int = Field(default=..., description="The organic rank of the competitor.")


class KeywordAttributes(BaseModel):
    """Keyword attributes for a specific ASIN."""

    country: str = Field(default=..., description="The country of the keyword.")
    name: str = Field(default=..., description="The name of the keyword.")
    primary_asin: str = Field(default=..., description="The primary ASIN of the keyword.")
    monthly_trend: float = Field(default=..., description="The monthly trend of the keyword.")
    monthly_search_volume_exact: int = Field(default=..., description="The monthly search volume exact of the keyword.")
    quarterly_trend: float = Field(default=..., description="The quarterly trend of the keyword.")
    monthly_search_volume_broad: int = Field(default=..., description="The monthly search volume broad of the keyword.")
    dominant_category: str = Field(default=..., description="The dominant category of the keyword.")
    recommended_promotions: int = Field(default=..., description="The recommended promotions of the keyword.")
    sp_brand_ad_bid: Optional[float] = Field(default=None, description="The SP brand ad bid of the keyword.")
    ppc_bid_broad: Optional[float] = Field(default=None, description="The PPC bid broad of the keyword.")
    ppc_bid_exact: Optional[float] = Field(default=None, description="The PPC bid exact of the keyword.")
    ease_of_ranking_score: int = Field(default=..., description="The ease of ranking score of the keyword.")
    relevancy_score: int = Field(default=..., description="The relevancy score of the keyword.")
    organic_product_count: int = Field(default=..., description="The organic product count of the keyword.")
    sponsored_product_count: int = Field(default=..., description="The sponsored product count of the keyword.")
    updated_at: datetime = Field(default=..., description="The date the keyword was last updated.")
    organic_rank: int = Field(default=..., description="The organic rank of the keyword.")
    sponsored_rank: Optional[int] = Field(default=None, description="The sponsored rank of the keyword.")
    overall_rank: Optional[int] = Field(default=None, description="The overall rank of the keyword.")
    organic_ranking_asins_count: int = Field(default=..., description="The organic ranking ASINs count of the keyword.")
    sponsored_ranking_asins_count: int = Field(
        default=..., description="The sponsored ranking ASINs count of the keyword."
    )
    avg_competitor_organic_rank: Optional[int] = Field(
        default=None, description="The average competitor organic rank of the keyword."
    )
    avg_competitor_sponsored_rank: Optional[int] = Field(
        default=None, description="The average competitor sponsored rank of the keyword."
    )
    relative_organic_position: int = Field(default=..., description="The relative organic position of the keyword.")
    relative_sponsored_position: int = Field(default=..., description="The relative sponsored position of the keyword.")
    competitor_organic_rank: List[CompetitorRank] = Field(
        default=..., description="The competitor organic rank of the keyword."
    )
    variation_lowest_organic_rank: Optional[int] = Field(
        default=None, description="The variation lowest organic rank of the keyword."
    )

    @field_serializer("updated_at")
    def _serialize_updated_at(self, v: datetime):  # noqa: PLR6301
        return serialize_datetime(v)


class KeywordByASIN(BaseModel):
    """represents a response object containing keyword data for a specific asin."""

    id: str = Field(default=..., description="The ID of the keyword.")
    type: str = Field(default=..., description="The type of the keyword.")
    attributes: KeywordAttributes = Field(default=..., description="The attributes for the keyword.")
