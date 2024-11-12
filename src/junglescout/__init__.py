"""Jungle Scout Client package.

This package contains the Jungle Scout Client package.
"""

__all__ = ["Client", "ClientAsync", "ClientSync"]
__version__ = "0.4.0"

from .client_async import ClientAsync
from .client_sync import ClientSync

# Importing Client from client_sync for backwards compatibility. This will be removed in the next major release.
Client = ClientSync
