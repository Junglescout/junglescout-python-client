from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class APIResponseError(BaseModel):
    """Represents an error in a response from the Jungle Scout API."""

    title: str = Field(default=..., description="The title of the error.")
    detail: str = Field(default=..., description="The detail of the error.")
    code: str = Field(default=..., description="The code of the error.")
    status: str = Field(default=..., description="The status code for the error.")


class APIResponseLink(BaseModel):
    """Represents the links for a response from the Jungle Scout API."""

    self: Optional[str] = Field(default=None, description="The current link.")
    next: Optional[str] = Field(default=None, description="The next link.")


class APIResponseMeta(BaseModel):
    """Represents additional metadata for a response from the Jungle Scout API."""

    total_items: Optional[int] = Field(default=None, description="The total number of items in the response.")
    errors: Optional[List[APIResponseError]] = Field(default=None, description="The errors in the response.")


class APIResponse(BaseModel, Generic[DataT]):
    """Represents a response from the Jungle Scout API."""

    data: DataT = Field(default=None, description="The data associated with the response.")
    links: APIResponseLink = Field(default=None, description="The links for the response.")
    meta: APIResponseMeta = Field(default=None, description="Additional metadata for the response.")
