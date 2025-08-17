"""Filmot module"""

__all__ = ["filmot"]

from ..requests import get_soup

FILMOT_BASE_URL = "filmot.com"


class filmot:
    @staticmethod
    def get_video():
        get_soup(f"{FILMOT_BASE_URL}")

    @staticmethod
    def get_channel(id: str):
        lol = get_soup(f"{FILMOT_BASE_URL}/channel/{id}")
        print(lol)
