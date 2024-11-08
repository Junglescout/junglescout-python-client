from junglescout.models.parameters.marketplace import Marketplace
from junglescout.models.requests.historical_search_volume_request import (
    HistoricalSearchVolumeArgs,
)


def test_historical_search_volume_args():
    args = HistoricalSearchVolumeArgs(
        keyword="keyword",
        marketplace=Marketplace.US,
        sort_option=None,
        start_date="2021-01",
        end_date="2021-02",
    )
    assert args.model_dump(by_alias=True, exclude_none=True) == {
        "keyword": "keyword",
        "marketplace": Marketplace.US,
        "start_date": "2021-01",
        "end_date": "2021-02",
    }
