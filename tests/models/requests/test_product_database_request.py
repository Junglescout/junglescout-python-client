from junglescout.models.parameters.marketplace import Marketplace
from junglescout.models.parameters.product_tiers import ProductTiers
from junglescout.models.parameters.seller_types import SellerTypes
from junglescout.models.requests.product_database_request import ProductDatabaseArgs


def test_product_database_args():
    args = ProductDatabaseArgs(
        include_keywords=None,
        exclude_keywords=None,
        collapse_by_parent=None,
        categories=None,
        product_tiers=None,
        seller_types=None,
        product_filter_options=None,
        product_sort_option=None,
        marketplace=Marketplace.US,
        page_size=None,
        page=None,
    )
    assert args.model_dump(by_alias=True, exclude_none=True) == {
        "page_size": 10,
        "exclude_keywords": [],
        "marketplace": Marketplace.US,
        "product_tiers": [
            ProductTiers.OVERSIZE,
            ProductTiers.STANDARD,
        ],
        "seller_types": [
            SellerTypes.AMZ,
            SellerTypes.FBA,
            SellerTypes.FBM,
        ],
    }
