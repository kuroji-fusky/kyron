import colorama  # type: ignore
from typing import Any, Optional

__all__ = ["kyron_tables"]

AnyDict = dict[str, Any]


class kyron_tables:
    """
    A nifty class for generating tables from da terminal
    """

    def __init__(self, *,
                 heading: Optional[str] = None,
                 footnotes: Optional[str] = None) -> None:
        pass

    def set_data(self, _data: AnyDict, *, dump_file: str):
        pass
