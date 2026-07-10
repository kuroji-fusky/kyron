import platform
from typing import Final

os_t = platform.system().lower()

IS_WINDOWS: Final = os_t == "windows"
IS_MACOS: Final = os_t == "darwin"
IS_LINUX: Final = os_t == "linux"
