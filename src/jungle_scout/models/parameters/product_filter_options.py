from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class ProductFilterOptions(BaseModel):
    """Represents the filter options for product filtering. This class is used to filter products based on their attributes, used on Product Database.

    Attributes:
        exclude_top_brands (Optional[bool]): Whether to exclude top brands.
        exclude_unavailable_products (Optional[bool]): Whether to exclude unavailable products.
        min_price (Optional[int]): The minimum price of the products.
        max_price (Optional[int]): The maximum price of the products.
        min_net (Optional[int]): The minimum net value of the products.
        max_net (Optional[int]): The maximum net value of the products.
        min_rank (Optional[int]): The minimum rank of the products.
        max_rank (Optional[int]): The maximum rank of the products.
        min_sales (Optional[int]): The minimum sales of the products.
        max_sales (Optional[int]): The maximum sales of the products.
        min_revenue (Optional[int]): The minimum revenue of the products.
        max_revenue (Optional[int]): The maximum revenue of the products.
        min_reviews (Optional[int]): The minimum number of reviews of the products.
        max_reviews (Optional[int]): The maximum number of reviews of the products.
        min_rating (Optional[int]): The minimum rating of the products.
        max_rating (Optional[int]): The maximum rating of the products.
        min_weight (Optional[int]): The minimum weight of the products.
        max_weight (Optional[int]): The maximum weight of the products.
        min_sellers (Optional[int]): The minimum number of sellers of the products.
        max_sellers (Optional[int]): The maximum number of sellers of the products.
        min_lqs (Optional[int]): The minimum LQS (Listing Quality Score) of the products.
        max_lqs (Optional[int]): The maximum LQS (Listing Quality Score) of the products.
        min_updated_at (Optional[str]): The minimum updated date of the products in the format "YYYY-MM-DD".
        max_updated_at (Optional[str]): The maximum updated date of the products in the format "YYYY-MM-DD".
    """

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

    @field_validator("min_updated_at", "max_updated_at")
    def _validate_date_format(cls, v):
        if v:
            try:
                datetime.strptime(v, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return v
