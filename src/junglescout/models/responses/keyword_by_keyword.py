from typing import Optional

from pydantic import BaseModel, Field


class KeywordByKeywordAttributes(BaseModel):
    """Attributes for keyword."""

    country: str = Field(default=..., description="The country of the keyword.")
    name: str = Field(default=..., description="The name of the keyword.")
    monthly_trend: Optional[float] = Field(default=None, description="The monthly trend of the keyword.")
    monthly_search_volume_exact: Optional[int] = Field(
        default=None, description="The monthly search volume exact of the keyword."
    )
    quarterly_trend: Optional[float] = Field(default=None, description="The quarterly trend of the keyword.")
    monthly_search_volume_broad: Optional[int] = Field(
        default=None, description="The monthly search volume broad of the keyword."
    )
    dominant_category: Optional[str] = Field(default=None, description="The dominant category of the keyword.")
    recommended_promotions: Optional[int] = Field(default=..., description="The recommended promotions of the keyword.")
    sp_brand_ad_bid: Optional[float] = Field(default=None, description="The SP brand ad bid of the keyword.")
    ppc_bid_broad: Optional[float] = Field(default=None, description="The PPC bid broad of the keyword.")
    ppc_bid_exact: Optional[float] = Field(default=None, description="The PPC bid exact of the keyword.")
    ease_of_ranking_score: Optional[int] = Field(default=None, description="The ease of ranking score of the keyword.")
    relevancy_score: Optional[int] = Field(default=None, description="The relevancy score of the keyword.")
    organic_product_count: Optional[int] = Field(default=None, description="The organic product count of the keyword.")
    sponsored_product_count: Optional[int] = Field(
        default=None, description="The sponsored product count of the keyword."
    )


class KeywordByKeyword(BaseModel):
    """Represents a response object containing keyword data."""

    id: str = Field(default=..., description="The ID of the keyword.")
    type: str = Field(default=..., description="The type of the keyword.")
    attributes: KeywordByKeywordAttributes = Field(default=..., description="Attributes for the response.")
