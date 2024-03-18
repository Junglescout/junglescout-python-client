from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class APIResponseLink(BaseModel):
    self: str = Field(default=..., description="The current link.")
    next: str = Field(default=..., description="The next link.")


class APIResponseMeta(BaseModel):
    total_items: int = Field(default=..., description="The total number of items in the response.")


class APIResponse(BaseModel, Generic[DataT]):
    """Represents a response from the Jungle Scout API."""

    data: DataT = Field(default=None, description="The data associated with the response.")
    links: APIResponseLink = Field(default=None, description="The links for the response.")
    meta: APIResponseMeta = Field(default=None, description="Additional metadata for the response.")
