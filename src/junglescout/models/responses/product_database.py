from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, field_serializer

from .serializer_helpers import serialize_date, serialize_datetime


class ProductDatabaseSubcategoryRanks(BaseModel):
    """Represents a response object containing subcategory ranks."""

    subcategory: str = Field(default=..., description="The subcategory of the product.")
    rank: int = Field(default=..., description="The rank of the product.")


class ProductDatabaseFeeBreakdown(BaseModel):
    """Represents a response object containing fee breakdown."""

    fba_fee: float = Field(default=..., description="The FBA fee of the product.")
    referral_fee: float = Field(default=..., description="The referral fee of the product.")
    variable_closing_fee: float = Field(default=..., description="The variable closing fee of the product.")
    total_fees: float = Field(default=..., description="The total fees of the product.")


class ProductDatabaseAttributes(BaseModel):
    """Product database attributes."""

    title: str = Field(default=..., description="The title of the product.")
    price: Optional[float] = Field(default=None, description="The price of the product.")
    reviews: Optional[int] = Field(default=None, description="The number of reviews for the product.")
    category: Optional[str] = Field(default=None, description="The category of the product.")
    rating: Optional[float] = Field(default=None, description="The rating of the product.")
    image_url: Optional[str] = Field(default=None, description="The image URL of the product.")
    parent_asin: Optional[str] = Field(default=None, description="The parent ASIN of the product.")
    is_variant: Optional[bool] = Field(default=None, description="Whether the product is a variant.")
    seller_type: Optional[str] = Field(default=None, description="The type of the seller.")
    variants: Optional[List[str]] = Field(default=None, description="The number of variants for the product.")
    is_standalone: Optional[bool] = Field(default=None, description="Whether the product is standalone.")
    is_parent: Optional[bool] = Field(default=None, description="Whether the product is a parent.")
    brand: Optional[str] = Field(default=None, description="The brand of the product.")
    product_rank: Optional[int] = Field(default=None, description="The rank of the product.")
    weight_value: Optional[float] = Field(default=None, description="The weight value of the product.")
    weight_unit: Optional[str] = Field(default=None, description="The weight unit of the product.")
    length_value: Optional[float] = Field(default=None, description="The length value of the product.")
    width_value: Optional[float] = Field(default=None, description="The width value of the product.")
    height_value: Optional[float] = Field(default=None, description="The height value of the product.")
    dimensions_unit: Optional[str] = Field(default=None, description="The dimensions unit of the product.")
    listing_quality_score: Optional[float] = Field(
        default=None, description="The listing quality score of the product."
    )
    number_of_sellers: Optional[int] = Field(default=None, description="The number of sellers for the product.")
    buy_box_owner: Optional[str] = Field(default=None, description="The buy box owner of the product.")
    buy_box_owner_seller_id: Optional[str] = Field(
        default=None, description="The buy box owner seller ID of the product."
    )
    date_first_available: Optional[datetime] = Field(
        default=None, description="The date the product was first available."
    )
    date_first_available_is_estimated: Optional[bool] = Field(
        default=None, description="Whether the date the product was first available is estimated."
    )
    approximate_30_day_revenue: Optional[float] = Field(
        default=None, description="The approximate 30 day revenue of the product."
    )
    approximate_30_day_units_sold: Optional[int] = Field(
        default=None, description="The approximate 30 day units sold of the product."
    )
    ean_list: Optional[List[int]] = Field(default=None, description="The EAN list of the product.")
    variant_reviews: Optional[int] = Field(default=None, description="The variant reviews of the product.")
    updated_at: datetime = Field(default=..., description="The date the product was last updated.")
    subcategory_ranks: Optional[List[ProductDatabaseSubcategoryRanks]] = Field(
        default=None, description="The subcategory ranks of the product."
    )
    fee_breakdown: Optional[ProductDatabaseFeeBreakdown] = Field(
        default=None, description="The fee breakdown of the product."
    )

    @field_serializer("updated_at")
    def _serialize_updated_at(self, v: datetime):  # noqa: PLR6301
        return serialize_datetime(v)

    @field_serializer("date_first_available")
    def _serialize_date_first_available(self, v: datetime):  # noqa: PLR6301
        return serialize_date(v)


class ProductDatabase(BaseModel):
    """Represents a response from the product database API."""

    id: str = Field(default=..., description="The ID of the product.")
    type: str = Field(default=..., description="The type of the product.")
    attributes: ProductDatabaseAttributes
