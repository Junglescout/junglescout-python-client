from pydantic import BaseModel, Field


class KeywordByKeywordAttributes(BaseModel):
    """Attributes for keyword."""

    country: str = Field(default=..., description="The country of the keyword.")
    name: str = Field(default=..., description="The name of the keyword.")
    monthly_trend: int = Field(default=..., description="The monthly trend of the keyword.")
    monthly_search_volume_exact: int = Field(default=..., description="The monthly search volume exact of the keyword.")
    quarterly_trend: int = Field(default=..., description="The quarterly trend of the keyword.")
    monthly_search_volume_broad: int = Field(default=..., description="The monthly search volume broad of the keyword.")
    dominant_category: str = Field(default=..., description="The dominant category of the keyword.")
    recommended_promotions: str = Field(default=..., description="The recommended promotions of the keyword.")
    sp_brand_ad_bid: int = Field(default=..., description="The SP brand ad bid of the keyword.")
    ppc_bid_broad: int = Field(default=..., description="The PPC bid broad of the keyword.")
    ppc_bid_exact: int = Field(default=..., description="The PPC bid exact of the keyword.")
    ease_of_ranking_score: int = Field(default=..., description="The ease of ranking score of the keyword.")
    relevancy_score: int = Field(default=..., description="The relevancy score of the keyword.")
    organic_product_count: int = Field(default=..., description="The organic product count of the keyword.")
    sponsored_product_count: int = Field(default=..., description="The sponsored product count of the keyword.")


class KeywordByKeyword(BaseModel):
    """Represents a response object containing keyword data."""

    links: str = Field(default=..., description="The links for the response.")
    meta: str = Field(default=..., description="The metadata for the response.")
    id: str = Field(default=..., description="The ID of the keyword.")
    type: str = Field(default=..., description="The type of the keyword.")
    attributes: KeywordByKeywordAttributes = Field(default=..., description="Attributes for the response.")
