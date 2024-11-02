"""Jungle Scout Client package.

This package contains the Jungle Scout Client package.
"""

__all__ = ["Client", "ClientAsync", "ClientSync"]
__version__ = "0.2.2"

from .client_async import ClientAsync
from .client_sync import ClientSync

Client = ClientSync
