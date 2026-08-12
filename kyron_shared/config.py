from typing import TypedDict, NotRequired, Literal

__all__ = [
    "ArchiveType",
    "KYRON_DIRECTORY_CONTENTS",
    "KyronConfig",
    "KyronAppConfig"
]

KYRON_DIRECTORY_CONTENTS = [
    "logs/",
    "avatars/",
    "config.json"
]

ArchiveType = Literal["channel", "playlist", "ia_mirror"]


class KyronConfig(TypedDict):
    """Used under `.kyron/config.json`"""

    type: ArchiveType
    storeAvatars: NotRequired[bool]
    lastUpdate: NotRequired[str]


class KyronAppConfig(TypedDict):
    """The global application config"""
    ...
