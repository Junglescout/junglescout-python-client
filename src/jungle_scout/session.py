import urllib.parse
from typing import Dict, Optional
from jungle_scout.models.parameters.api_type import ApiType
import requests


class Session(requests.Session):
    def __init__(self, default_connect_timeout=4, default_read_timeout=10):
        super().__init__()
        self.default_connect_timeout = default_connect_timeout
        self.default_read_timeout = default_read_timeout
        self.headers.update(
            {
                "Accept": "application/vnd.junglescout.v1+json",
                "Content-Type": "application/vnd.api+json",
            }
        )
        self.base_url = "https://developer.junglescout.com/api"

    def build_url(self, *args, params: Optional[Dict] = None):
        parts = [self.base_url]
        parts.extend(args)
        parts = [str(p) for p in parts]
        url = "/".join(parts)
        if params:
            return f"{url}?{urllib.parse.urlencode(params)}"
        return url

    def login(self, api_key_name: str, api_key: str, api_type: Optional[ApiType] = ApiType.JS):
        self.headers.update(
            {
                "Authorization": f"{api_key_name}:{api_key}",
                "X_API_Type": api_type.value
            }
        )
