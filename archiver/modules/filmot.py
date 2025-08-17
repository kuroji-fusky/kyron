"""Filmot module"""

from utils.requests import get_soup  # type: ignore

FILMOT_BASE_URL = "filmot.com"


class filmot:
    @staticmethod
    def get_video():
        get_soup(f"{FILMOT_BASE_URL}")

    @staticmethod
    def get_channel(id: str):
        lol = get_soup(f"{FILMOT_BASE_URL}/channel/{id}")
        print(lol)
