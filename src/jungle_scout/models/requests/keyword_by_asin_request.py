from jungle_scout.base_request import BaseRequest
from typing import Dict, List, Optional, Union, TypedDict
from jungle_scout.models.parameters.filter_options import FilterOptions
from jungle_scout.models.parameters.sort import Sort
import json


class KeywordByAsinParams(TypedDict):
    marketplace: str
    sort: Optional[Sort]
    page_size: int = 50
    page: Optional[str]


class KeywordByAsinAttributes(TypedDict):
    asins: List[str]
    include_variants: bool
    filter_options: Optional[FilterOptions]


class KeywordByAsinRequest(BaseRequest):
    def __init__(self, asin: Union[str, List[str]], params: KeywordByAsinParams, attributes: KeywordByAsinAttributes):
        self.method = 'POST'
        self.type = 'keywords_by_asin_query'
        self.asin = self._resolve_asin(asin)
        self.params = self.build_params(params)
        self.payload = self.build_payload(attributes)

    def build_payload(self, attributes: KeywordByAsinAttributes) -> str:
        attributes_dict = {"asins": self.asin, "include_variants": attributes.get(
            'include_variants')
        }

        if attributes.get('filter_options'):
            attributes_dict.update(vars(attributes.get('filter_options')))

        clean_attributes = {k: v for k,
                            v in attributes_dict.items() if v is not None}

        return json.dumps(
            {
                "data": {
                    "type": self.type,
                    "attributes": clean_attributes
                }
            }
        )

    def build_params(self, params: KeywordByAsinParams) -> Dict:
        params_dict = {
            "marketplace": params.get('marketplace'),
            "sort": params.get('sort'),
            "page[size]": params.get('page_size', 50),
            "page[cursor]": params.get('page')
        }

        clean_params = {k: v for k,
                        v in params.items() if v is not None}

        return clean_params

    def _resolve_asin(self, provided_asin: Union[str, List[str]]) -> List[str]:
        if isinstance(provided_asin, str):
            return [provided_asin]
        elif isinstance(provided_asin, list):
            if len(provided_asin) > 10:
                raise AttributeError("ASIN list cannot exceed 10")
            return provided_asin
        else:
            raise AttributeError("ASIN cannot be resolved")
