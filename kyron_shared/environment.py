from platform import system
from pathlib import Path
from typing import Optional

from kyron_shared.cmd import KyronCommandScaffolder


__all__ = [
    "is_linux",
    "is_macos",
    "is_windows",
    "KyronBaseEnvironment"
]


is_linux = system() == "Linux"
is_windows = system() == "Windows"
is_macos = system() == "macOS"

OptionalPath = Optional[Path | str]


class KyronBaseEnvironment:
    """
    Kyron doesn't come with FFmpeg or yt-dlp built-in, the user must come with it pre-installed
    on their system by detecting their path environments. Otherwise, they'll need to specify a path
    as they are required for Kyron to function fully
    """

    def __init__(self,
                 *,
                 ffmpeg_dir: OptionalPath = None,
                 ytdlp_dir: OptionalPath = None):
        self.detected_os = system() or "Linux"

        # todo: for `has_*` methods; cache result from a top-level .kyron_global config so this function gets ran once
        self.ffmpeg_dir = KyronCommandScaffolder.detect_exec("ffmpeg")   # noqa
        self.ytdlp_dir = KyronCommandScaffolder.detect_exec("yt-dlp")   # noqa

    def has_ffmpeg(self):
        return bool(self.ffmpeg_dir)

    def has_ytdlp(self):
        return bool(self.ytdlp_dir)
