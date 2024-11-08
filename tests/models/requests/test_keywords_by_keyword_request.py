from junglescout.models.parameters import Marketplace
from junglescout.models.requests.keywords_by_keyword_request import (
    KeywordsByKeywordArgs,
)


def test_keywords_by_keyword_args():
    args = KeywordsByKeywordArgs(
        search_terms="test",
        categories=["test"],
        filter_options=None,
        sort_option=None,
        marketplace=Marketplace.US,
        page=None,
        page_size=None,
    )
    assert args.model_dump(exclude_none=True, by_alias=True) == {
        "search_terms": "test",
        "categories": ["test"],
        "marketplace": Marketplace.US,
    }
