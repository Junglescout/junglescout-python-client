from junglescout.models.parameters.marketplace import Marketplace
from junglescout.models.requests.share_of_voice_request import ShareOfVoiceArgs


def test_share_of_voice_args():
    args = ShareOfVoiceArgs(keyword="keyword", marketplace=Marketplace.US)
    assert args.model_dump(exclude_none=True, by_alias=True) == {
        "keyword": "keyword",
        "marketplace": Marketplace.US,
    }
