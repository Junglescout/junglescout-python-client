from typing import Optional

from pydantic import BaseModel, Field, validator


class ProductFilterOptions(BaseModel):
    exclude_top_brands: Optional[bool] = Field(None)
    exclude_unavailable_products: Optional[bool] = Field(None)
    min_price: Optional[int] = Field(None, ge=0)
    max_price: Optional[int] = Field(None, ge=0)
    min_net: Optional[int] = Field(None, ge=0)
    max_net: Optional[int] = Field(None, ge=0)
    min_rank: Optional[int] = Field(None, ge=0)
    max_rank: Optional[int] = Field(None, ge=0)
    min_sales: Optional[int] = Field(None, ge=0)
    max_sales: Optional[int] = Field(None, ge=0)
    min_revenue: Optional[int] = Field(None, ge=0)
    max_revenue: Optional[int] = Field(None, ge=0)
    min_reviews: Optional[int] = Field(None, ge=0)
    max_reviews: Optional[int] = Field(None, ge=0)
    min_rating: Optional[int] = Field(None, ge=0)
    max_rating: Optional[int] = Field(None, ge=0)
    min_weight: Optional[int] = Field(None, ge=0)
    max_weight: Optional[int] = Field(None, ge=0)
    min_sellers: Optional[int] = Field(None, ge=0)
    max_sellers: Optional[int] = Field(None, ge=0)
    min_lqs: Optional[int] = Field(None, ge=0)
    max_lqs: Optional[int] = Field(None, ge=0)
    min_updated_at: Optional[str] = Field(None)
    max_updated_at: Optional[str] = Field(None)

    # validate min_update_at and max_updated_at to only accept date format in the form of "YYYY-MM-DD"
    @validator("min_updated_at", "max_updated_at", pre=True)
    def validate_date_format(cls, v):
        if v:
            try:
                datetime.strptime(v, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return v
