from typing import Optional

from pydantic import BaseModel

from junglescout.models.parameters.filter_options import FilterOptions


class Attributes(BaseModel):
    """Base model class with the basic attributes for filtering options.

    Attributes:
        - filter_options: The filter options for attributes. Must be a valid FilterOptions object.
    """

    filter_options: Optional[FilterOptions] = None
