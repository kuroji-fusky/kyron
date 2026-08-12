from .fs import path_to_str
from .platform import is_windows
import shutil
import os
from platform import system
from pathlib import Path


class KyronBaseEnvironment:
    """
    Kyron doesn't come with FFmpeg or yt-dlp built-in, the user must come with it pre-installed
    on their system by detecting their path environments. Otherwise, they'll need to specify a path
    as they are required for Kyron to function fully
    """

    def __init__(self, *, ffmpeg_dir: OptionalPath = None, ytdlp_dir: OptionalPath = None):
        self.detected_os = system() or "Linux"

        # todo: for `has_*` methods; cache result from a top-level .kyron_global config so this function gets ran once
        self.ffmpeg_dir = self.detect_exec("ffmpeg")   # noqa
        self.ytdlp_dir = self.detect_exec("yt-dlp")   # noqa

    def detect_exec(self, exec: str):
        """A wrapper for `shutil.which` then fallbacks to `os.environ.get(...)`, otherwise, returns None"""
        initial_exec_detect = shutil.which(exec)

        if initial_exec_detect is not None:
            return initial_exec_detect

        env_path_separator = ";" if is_windows else ":"
        env_paths = os.environ.get("PATH", "").split(env_path_separator)

        for dir in env_paths:
            if not dir:
                continue

            parsed_path = Path(dir) / exec

            if parsed_path.is_file() and os.access(parsed_path, os.X_OK):
                return path_to_str(parsed_path)

        return None

    def has_ffmpeg(self):
        return bool(self.ffmpeg_dir)

    def has_ytdlp(self):
        return bool(self.ytdlp_dir)
