from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class ProductFilterOptions(BaseModel):
    exclude_top_brands: Optional[bool] = None
    exclude_unavailable_products: Optional[bool] = None
    min_price: Optional[int] = None
    max_price: Optional[int] = None
    min_net: Optional[int] = None
    max_net: Optional[int] = None
    min_rank: Optional[int] = None
    max_rank: Optional[int] = None
    min_sales: Optional[int] = None
    max_sales: Optional[int] = None
    min_revenue: Optional[int] = None
    max_revenue: Optional[int] = None
    min_reviews: Optional[int] = None
    max_reviews: Optional[int] = None
    min_rating: Optional[int] = None
    max_rating: Optional[int] = None
    min_weight: Optional[int] = None
    max_weight: Optional[int] = None
    min_sellers: Optional[int] = None
    max_sellers: Optional[int] = None
    min_lqs: Optional[int] = None
    max_lqs: Optional[int] = None
    min_updated_at: Optional[str] = None
    max_updated_at: Optional[str] = None

    # validate min_update_at and max_updated_at to only accept date format in the form of "YYYY-MM-DD"
    @field_validator("min_updated_at", "max_updated_at")
    def validate_date_format(cls, v):
        if v:
            try:
                datetime.strptime(v, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return v
