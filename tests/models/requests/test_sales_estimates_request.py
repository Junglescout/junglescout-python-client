from junglescout.models.parameters.marketplace import Marketplace
from junglescout.models.requests.sales_estimates_request import SalesEstimatesArgs


def test_sales_estimates_args():
    args = SalesEstimatesArgs(
        asin="test",
        start_date="2021-01-01",
        end_date="2021-01-01",
        sort_option=None,
        marketplace=Marketplace.US,
    )
    assert args.model_dump(exclude_none=True, by_alias=True) == {
        "asin": "test",
        "start_date": "2021-01-01",
        "end_date": "2021-01-01",
        "marketplace": Marketplace.US,
    }
