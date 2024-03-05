from typing import TypedDict, Optional


class Options(TypedDict):
    min_monthly_search_volume_exact: Optional[int]
    max_monthly_search_volume_exact: Optional[int]
    min_monthly_search_volume_broad: Optional[int]
    max_monthly_search_volume_broad: Optional[int]
    min_word_count: Optional[int]
    max_word_count: Optional[int]
    min_organic_product_count: Optional[int]
    max_organic_product_count: Optional[int]


class FilterOptions:
    def __init__(self, options: Options):
        self._update_options(options)

    def _update_options(self, options: Options):
        self.min_monthly_search_volume_exact = options.get(
            "min_monthly_search_volume_exact")
        self.max_monthly_search_volume_exact = options.get(
            "max_monthly_search_volume_exact")
        self.min_monthly_search_volume_broad = options.get(
            "min_monthly_search_volume_broad")
        self.max_monthly_search_volume_broad = options.get(
            "max_monthly_search_volume_broad")
        self.min_word_count = options.get("min_word_count")
        self.max_word_count = options.get("max_word_count")
        self.min_organic_product_count = options.get(
            "min_organic_product_count")
        self.max_organic_product_count = options.get(
            "max_organic_product_count")
