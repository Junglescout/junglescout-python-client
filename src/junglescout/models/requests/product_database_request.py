from typing import Any, Dict, List, Optional

from pydantic import (
    BaseModel,
    Field,
    ValidationInfo,
    field_serializer,
    field_validator,
    model_serializer,
)

from junglescout.models.default_if_none import DefaultIfNone
from junglescout.models.parameters import (
    Attributes,
    Marketplace,
    Params,
    ProductFilterOptions,
    ProductSort,
    ProductTiers,
    SellerTypes,
)
from junglescout.models.requests.method import Method
from junglescout.models.requests.request import Request
from junglescout.session import Session


class ProductDatabaseArgs(BaseModel):
    include_keywords: Optional[List[str]]
    exclude_keywords: DefaultIfNone[List[str]] = Field(default_factory=list)
    categories: Optional[List[str]]
    product_tiers: DefaultIfNone[List[ProductTiers]] = Field(
        default_factory=lambda: [ProductTiers.OVERSIZE, ProductTiers.STANDARD]
    )
    seller_types: DefaultIfNone[List[SellerTypes]] = Field(
        default_factory=lambda: [SellerTypes.AMZ, SellerTypes.FBA, SellerTypes.FBM]
    )
    product_filter_options: Optional[ProductFilterOptions]
    product_sort_option: Optional[ProductSort]
    marketplace: Marketplace
    page_size: DefaultIfNone[int] = Field(default=10)
    page: Optional[str] = None


class ProductDatabaseParams(Params):
    product_sort_option: Optional[ProductSort] = None

    @field_serializer("product_sort_option")
    def serialize_product_sort(self, value: Optional[ProductSort]):  # noqa: PLR6301
        return value.value if value else None


class ProductDatabaseAttributes(Attributes):
    marketplace: Marketplace
    include_keywords: Optional[List[str]] = None
    exclude_keywords: Optional[List[str]] = None
    seller_types: Optional[List[SellerTypes]] = None
    product_tiers: Optional[List[ProductTiers]] = None
    product_filter_options: Optional[ProductFilterOptions] = None
    categories: Optional[List[str]] = None

    @field_validator("categories")
    @classmethod
    def validate_categories(cls, v: Optional[List[str]], info: ValidationInfo) -> Optional[List[str]]:
        marketplace = info.data["marketplace"]
        if v:
            for category in v:
                assert category in marketplace.categories, f"Category '{category}' not found in marketplace categories"
        return v

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        serialized_model = {
            "exclude_keywords": self.exclude_keywords,
            "include_keywords": self.include_keywords,
            "categories": self.categories or self.marketplace.categories,
        }

        if self.product_tiers is not None:
            serialized_model["product_tiers"] = [tier.value for tier in self.product_tiers]

        if self.seller_types is not None:
            serialized_model["seller_types"] = [seller_type.value for seller_type in self.seller_types]

        if self.filter_options is not None:
            serialized_model.update(**self.filter_options.model_dump(exclude_none=True))

        if self.product_filter_options is not None:
            serialized_model.update(**self.product_filter_options.model_dump(exclude_none=True))

        return serialized_model


class ProductDatabaseRequest(Request[ProductDatabaseArgs, ProductDatabaseParams, ProductDatabaseAttributes]):
    @property
    def url(self) -> str:
        return self.session.build_url("product_database_query", params=self.params_serialized)

    @property
    def method(self) -> Method:
        return Method.POST

    def serialize_params(self) -> Dict:
        return self.params.model_dump(by_alias=True, exclude_none=True)

    def serialize_payload(self) -> Dict:
        return {
            "data": {
                "type": "product_database_query",
                "attributes": self.attributes.model_dump(by_alias=True, exclude_none=True),
            }
        }

    @classmethod
    def from_args(cls, args: ProductDatabaseArgs, session: Session) -> "ProductDatabaseRequest":
        params = ProductDatabaseParams(
            marketplace=args.marketplace,
            product_sort_option=args.product_sort_option,
            page_size=args.page_size,
            page=args.page,
        )
        attributes = ProductDatabaseAttributes(
            marketplace=args.marketplace,
            include_keywords=args.include_keywords,
            exclude_keywords=args.exclude_keywords,
            categories=args.categories,
            product_tiers=args.product_tiers,
            seller_types=args.seller_types,
            product_filter_options=args.product_filter_options,
        )
        return cls(params=params, attributes=attributes, session=session)
