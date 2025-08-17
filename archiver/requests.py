"""A wrapper for `requests.Session` and `BeautifulSoup`."""

from typing import Optional, Any
import json

import requests
from bs4 import BeautifulSoup

rs = requests.Session()


HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "For an archival project"
}

HTTPS_SCHEMA = "https://"


def get_call(url: str, *, params: Optional[dict] = None):
    return rs.get(f"{HTTPS_SCHEMA}{url}", params=params, headers=HEADERS)


def post_call(url, params: Optional[dict], json_payload: dict[str, Any]):
    return rs.post(f"{HTTPS_SCHEMA}{url}", params=params, json=json.dumps(json_payload), headers=HEADERS)


def get_soup(url: str, *, params: Optional[dict] = None):
    _req = get_call(url, params=params)

    return BeautifulSoup(_req.text, "html.parser")
