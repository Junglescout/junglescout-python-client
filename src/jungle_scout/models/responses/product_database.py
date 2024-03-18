from datetime import datetime

from pydantic import BaseModel, Field


class SubcategoryRanks(BaseModel):
    """Represents a response object containing subcategory ranks."""

    subcategory: str = Field(default=..., description="")
    rank: str = Field(default=..., description="")


class FeeBreakdown(BaseModel):
    """Represents a response object containing fee breakdown."""

    fba_fee: int = Field(default=..., description="")
    referral_fee: int = Field(default=..., description="")
    variable_closing_fee: int = Field(default=..., description="")
    total_fees: int = Field(default=..., description="")


class ProductDatabaseAttributes(BaseModel):
    """Product database attributes"""

    title: str = Field(default=..., description="The title of the product.")
    price: int = Field(default=..., description="The price of the product.")
    reviews: int = Field(default=..., description="The number of reviews for the product.")
    category: str = Field(default=..., description="The category of the product.")
    rating: str = Field(default=..., description="The rating of the product.")
    image_url: str = Field(default=..., description="The image URL of the product.")
    parent_asin: str = Field(default=..., description="The parent ASIN of the product.")
    is_variant: bool = Field(default=..., description="Whether the product is a variant.")
    seller_type: str = Field(default=..., description="The type of the seller.")
    variants: str = Field(default=..., description="The variants of the product.")
    is_standalone: str = Field(default=..., description="Whether the product is standalone.")
    is_parent: str = Field(default=..., description="Whether the product is a parent.")
    brand: str = Field(default=..., description="The brand of the product.")
    product_rank: str = Field(default=..., description="The rank of the product.")
    weight_value: str = Field(default=..., description="The weight value of the product.")
    weight_unit: str = Field(default=..., description="The weight unit of the product.")
    length_value: str = Field(default=..., description="The length value of the product.")
    width_value: str = Field(default=..., description="The width value of the product.")
    height_value: str = Field(default=..., description="The height value of the product.")
    dimensions_unit: str = Field(default=..., description="The dimensions unit of the product.")
    listing_quality_score: str = Field(default=..., description="The listing quality score of the product.")
    number_of_sellers: str = Field(default=..., description="The number of sellers for the product.")
    buy_box_owner: str = Field(default=..., description="The buy box owner of the product.")
    buy_box_owner_seller_id: str = Field(default=..., description="The buy box owner seller ID of the product.")
    date_first_available: str = Field(default=..., description="The date the product was first available.")
    date_first_available_is_estimated: str = Field(
        default=..., description="Whether the date the product was first available is estimated."
    )
    approximate_30_day_revenue: str = Field(default=..., description="The approximate 30 day revenue of the product.")
    approximate_30_day_units_sold: str = Field(
        default=..., description="The approximate 30 day units sold of the product."
    )
    ean_list: str = Field(default=..., description="The EAN list of the product.")
    variant_reviews: str = Field(default=..., description="The variant reviews of the product.")
    updated_at: datetime = Field(default=..., description="The date the product was last updated.")
    subcategory_ranks: SubcategoryRanks = Field(default=..., description="The subcategory ranks of the product.")
    fee_breakdown: FeeBreakdown = Field(default=..., description="The fee breakdown of the product.")


class ProductDatabase(BaseModel):
    """Represents a response from the product database API."""

    links: str = Field(default=..., description="The links for the response.")
    meta: str = Field(default=..., description="The metadata for the response.")
    id: str = Field(default=..., description="The ID of the product.")
    type: str = Field(default=..., description="The type of the product.")
    attributes: ProductDatabaseAttributes
