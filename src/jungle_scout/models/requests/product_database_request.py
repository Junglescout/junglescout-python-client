import json
from typing import Any, Dict, List, Optional

from pydantic import ValidationInfo, field_serializer, field_validator, model_serializer

from jungle_scout.base_request import BaseRequest
from jungle_scout.models.parameters.attributes import Attributes
from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.params import Params
from jungle_scout.models.parameters.product_filter_options import ProductFilterOptions
from jungle_scout.models.parameters.product_sort import ProductSort
from jungle_scout.models.parameters.product_tiers import ProductTiers
from jungle_scout.models.parameters.seller_types import SellerTypes
from jungle_scout.models.requests.method import Method
from jungle_scout.models.requests.request_type import RequestType


class ProductDatabaseParams(Params):
    product_sort_option: Optional[ProductSort] = None

    @field_serializer("product_sort_option")
    def serialize_sort(self, value: Optional[ProductSort]):
        return value.value if value else None


class ProductDatabaseAttributes(Attributes):
    marketplace: Marketplace
    include_keywords: List[str]
    exclude_keywords: List[str]
    seller_types: List[SellerTypes]
    product_tiers: List[ProductTiers]
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
            "product_tiers": [tier.value for tier in self.product_tiers],
            "seller_types": [seller_type.value for seller_type in self.seller_types],
            "exclude_keywords": self.exclude_keywords,
            "include_keywords": self.include_keywords,
            "categories": self.categories or self.marketplace.categories,
        }

        if self.filter_options is not None:
            serialized_model.update(**self.filter_options.model_dump(exclude_none=True))

        if self.product_filter_options is not None:
            serialized_model.update(**self.product_filter_options.model_dump(exclude_none=True))

        return serialized_model


class ProductDatabaseRequest(BaseRequest[ProductDatabaseParams, ProductDatabaseAttributes]):
    @property
    def type(self):
        return RequestType.PRODUCT_DATABASE

    @property
    def method(self) -> Method:
        return Method.POST

    def build_params(self, params: ProductDatabaseParams) -> Dict:
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: ProductDatabaseAttributes) -> str:
        return json.dumps(
            {"data": {"type": self.type.value, "attributes": attributes.model_dump(by_alias=True, exclude_none=True)}}
        )
