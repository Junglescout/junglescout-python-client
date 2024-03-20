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

    country: Optional[str] = Field(default=None, description="The country of the keyword.")
    name: Optional[str] = Field(default=None, description="The name of the keyword.")
    primary_asin: Optional[str] = Field(default=None, description="The primary ASIN of the keyword.")
    monthly_trend: Optional[float] = Field(default=None, description="The monthly trend of the keyword.")
    monthly_search_volume_exact: Optional[int] = Field(
        default=None, description="The monthly search volume exact of the keyword."
    )
    quarterly_trend: Optional[float] = Field(default=None, description="The quarterly trend of the keyword.")
    monthly_search_volume_broad: Optional[int] = Field(
        default=None, description="The monthly search volume broad of the keyword."
    )
    dominant_category: Optional[str] = Field(default=None, description="The dominant category of the keyword.")
    recommended_promotions: Optional[int] = Field(
        default=None, description="The recommended promotions of the keyword."
    )
    sp_brand_ad_bid: Optional[float] = Field(default=None, description="The SP brand ad bid of the keyword.")
    ppc_bid_broad: Optional[float] = Field(default=None, description="The PPC bid broad of the keyword.")
    ppc_bid_exact: Optional[float] = Field(default=None, description="The PPC bid exact of the keyword.")
    ease_of_ranking_score: Optional[int] = Field(default=None, description="The ease of ranking score of the keyword.")
    relevancy_score: Optional[int] = Field(default=None, description="The relevancy score of the keyword.")
    organic_product_count: Optional[int] = Field(default=None, description="The organic product count of the keyword.")
    sponsored_product_count: Optional[int] = Field(
        default=None, description="The sponsored product count of the keyword."
    )
    updated_at: datetime = Field(default=..., description="The date the keyword was last updated.")
    organic_rank: Optional[int] = Field(default=None, description="The organic rank of the keyword.")
    sponsored_rank: Optional[int] = Field(default=None, description="The sponsored rank of the keyword.")
    overall_rank: Optional[int] = Field(default=None, description="The overall rank of the keyword.")
    organic_ranking_asins_count: Optional[int] = Field(
        default=None, description="The organic ranking ASINs count of the keyword."
    )
    sponsored_ranking_asins_count: Optional[int] = Field(
        default=None, description="The sponsored ranking ASINs count of the keyword."
    )
    avg_competitor_organic_rank: Optional[int] = Field(
        default=None, description="The average competitor organic rank of the keyword."
    )
    avg_competitor_sponsored_rank: Optional[int] = Field(
        default=None, description="The average competitor sponsored rank of the keyword."
    )
    relative_organic_position: Optional[int] = Field(
        default=None, description="The relative organic position of the keyword."
    )
    relative_sponsored_position: Optional[int] = Field(
        default=None, description="The relative sponsored position of the keyword."
    )
    competitor_organic_rank: Optional[List[CompetitorRank]] = Field(
        default=None, description="The competitor organic rank of the keyword."
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
