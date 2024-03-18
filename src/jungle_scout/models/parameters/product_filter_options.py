from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class ProductFilterOptions(BaseModel):
    """Represents the filter options for product filtering.

    This class is used to filter products based on their attributes, used on Product Database.

    Attributes:
        - exclude_top_brands: Whether to exclude top brands.
        - exclude_unavailable_products: Whether to exclude unavailable products.
        - min_price: The minimum price of the products.
        - max_price: The maximum price of the products.
        - min_net: The minimum net value of the products.
        - max_net: The maximum net value of the products.
        - min_rank: The minimum rank of the products.
        - max_rank: The maximum rank of the products.
        - min_sales: The minimum sales of the products.
        - max_sales: The maximum sales of the products.
        - min_revenue: The minimum revenue of the products.
        - max_revenue: The maximum revenue of the products.
        - min_reviews: The minimum number of reviews of the products.
        - max_reviews: The maximum number of reviews of the products.
        - min_rating: The minimum rating of the products.
        - max_rating: The maximum rating of the products.
        - min_weight: The minimum weight of the products.
        - max_weight: The maximum weight of the products.
        - min_sellers: The minimum number of sellers of the products.
        - max_sellers: The maximum number of sellers of the products.
        - min_lqs: The minimum LQS (Listing Quality Score) of the products.
        - max_lqs: The maximum LQS (Listing Quality Score) of the products.
        - min_updated_at: The minimum updated date of the products in the format "YYYY-MM-DD".
        - max_updated_at: The maximum updated date of the products in the format "YYYY-MM-DD".
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
    @classmethod
    def _validate_date_format(cls, v):
        if v:
            try:
                datetime.strptime(v, "%Y-%m-%d")  # noqa: DTZ007
            except ValueError as exc:
                msg = "Incorrect data format, should be YYYY-MM-DD"
                raise ValueError(msg) from exc
        return v
