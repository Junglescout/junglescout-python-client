from typing import Optional

from pydantic import BaseModel

from jungle_scout.models.parameters.filter_options import FilterOptions


class Attributes(BaseModel):
    filter_options: Optional[FilterOptions] = None
