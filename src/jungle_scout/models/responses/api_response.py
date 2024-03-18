from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class APIResponse(BaseModel, Generic[DataT]):
    """Represents a response from the Jungle Scout API."""

    data: Optional[List[DataT]] = Field(default=None, description="The data associated with the response.")
    total_items: int = Field(default=..., description="The total items included in the response.")
