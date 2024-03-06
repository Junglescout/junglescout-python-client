from typing import Optional

from pydantic import BaseModel, Field


class FilterOptions(BaseModel):
    min_monthly_search_volume_exact: Optional[int] = Field(default=None, ge=0)
    max_monthly_search_volume_exact: Optional[int] = Field(default=None, ge=0)
    min_monthly_search_volume_broad: Optional[int] = Field(default=None, ge=0)
    max_monthly_search_volume_broad: Optional[int] = Field(default=None, ge=0)
    min_word_count: Optional[int] = Field(default=None, ge=0)
    max_word_count: Optional[int] = Field(default=None, ge=0)
    min_organic_product_count: Optional[int] = Field(default=None, ge=0)
    max_organic_product_count: Optional[int] = Field(default=None, ge=0)
