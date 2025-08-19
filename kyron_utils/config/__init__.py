from ..constants import CWD
import os
import json
from constants import *  # type:ignore

__all__ = ["kyron_conf", "is_supported_config_files"]

KYRON_DEFAULT_CONFIG = {
    "shorts": {
        "include": False,
    },

    "livestreams": {
        "include": False,
        "length_limit": 0
    },

    "downloads": []
}


class kyron_conf:
    # wip stuff
    def __init__(self):
        pass

    @staticmethod
    def create_config(base_path: str = CWD):
        with open(os.path.join(base_path, ".kyron_config.json"), "w") as f:
            json.dump(KYRON_DEFAULT_CONFIG, f, indent=2)
