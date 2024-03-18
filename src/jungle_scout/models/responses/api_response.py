from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class APIResponseLink(BaseModel):
    self: str = Field(default=..., description="The current link.")
    next: str = Field(default=..., description="The next link.")


class APIResponse(BaseModel, Generic[DataT]):
    """Represents a response from the Jungle Scout API."""

    data: Optional[DataT] = Field(default=None, description="The data associated with the response.")
    total_items: int = Field(default=None, description="The total items included in the response.")
    links: APIResponseLink = Field(default=None, description="The links for the response.")
    meta: dict = Field(default=None, description="Additional metadata for the response.")
