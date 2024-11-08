from typing import Annotated, Any, TypeVar, Union

from pydantic import AfterValidator
from pydantic_core import PydanticUseDefault


def _default_if_none(value: Any) -> Any:
    """Pydantic validator that raises PydanticUseDefault if the value is None.

    See Also: https://github.com/pydantic/pydantic/issues/8972#issuecomment-2447162842
    """
    if value is None:
        raise PydanticUseDefault()
    return value


T = TypeVar("T")

DefaultIfNone = Annotated[Union[T, None], AfterValidator(_default_if_none)]
