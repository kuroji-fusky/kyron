"""
This bih is responsible for parsing the JSON config for custom downloads from multiple channels or something idk
"""
import json

_WHITELISTED_KEYS = [
    # global keys
    "downloads", "livestream", "shorts", "cookies",
    "check_thumbnails"

    # key only for `downloads`
    "handle",

    # key only for `livestream` and `shorts`
    "include",

    # keys appended only IN global keys defined
    "filter",
]
