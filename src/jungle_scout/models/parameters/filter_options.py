from typing import Optional

from pydantic import BaseModel, Field


class FilterOptions(BaseModel):
    """Represents the filter options for searching products.

    Attributes:
        - min_monthly_search_volume_exact: The minimum exact monthly search volume.
        - max_monthly_search_volume_exact: The maximum exact monthly search volume.
        - min_monthly_search_volume_broad: The minimum broad monthly search volume.
        - max_monthly_search_volume_broad: The maximum broad monthly search volume.
        - min_word_count: The minimum word count.
        - max_word_count: The maximum word count.
        - min_organic_product_count: The minimum organic product count.
        - max_organic_product_count: The maximum organic product count.

    Usage:
        FilterOptions(min_monthly_search_volume_exact=150)
    """

    min_monthly_search_volume_exact: Optional[int] = Field(default=None, ge=0)
    max_monthly_search_volume_exact: Optional[int] = Field(default=None, ge=0)
    min_monthly_search_volume_broad: Optional[int] = Field(default=None, ge=0)
    max_monthly_search_volume_broad: Optional[int] = Field(default=None, ge=0)
    min_word_count: Optional[int] = Field(default=None, ge=0)
    max_word_count: Optional[int] = Field(default=None, ge=0)
    min_organic_product_count: Optional[int] = Field(default=None, ge=0)
    max_organic_product_count: Optional[int] = Field(default=None, ge=0)
