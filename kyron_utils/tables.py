import colorama  # type: ignore
from typing import Any, Optional

AnyDict = dict[str, Any]


class table_maker:
    """
    A nifty mini-class for generating tables from da terminal
    """

    def __init__(self, *,
                 heading: Optional[str] = None,
                 footnotes: Optional[str] = None) -> None:
        pass

    def set_data(self, _data: AnyDict, *, dump_file: str):
        pass
