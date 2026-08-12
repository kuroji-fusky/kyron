from platform import system

__all__ = ["is_linux", "is_windows", "is_macos"]

is_linux = system() == "Linux"
is_windows = system() == "Windows"
is_macos = system() == "macOS"
