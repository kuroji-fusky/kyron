from typing import final, Optional


class ArchiveError(Exception):
    """Base exception for your mom"""
    pass


class InsufficentSpaceError(ArchiveError):
    """
    Exception raised when there is not enough disk space to complete the operation.

    This exception is thrown when the system detects insufficient storage space
    to download anymore videos.
    """

    def __init__(self,
                 required: Optional[int] = None,
                 available: Optional[str] = None,
                 msg: Optional[str] = None) -> None:
        if not msg:
            # This is only temporary
            def disk_format(x): return f"{x / 1_000_000:.2f} MB" if x else "unknown"  # noqa
            super().__init__(f"Not enough disk space: required {disk_format(required)}, available {disk_format(available)}")  # noqa

        super().__init__(msg)


@final
class LowSpaceError(InsufficentSpaceError):
    """
    Similar to `NotEnoughSpaceError`, this exception is thrown while a download
    operation is ongoing.
    """
    pass


@final
class APIRateLimitError(ArchiveError):
    """
    Raises when either the API or its modules it depends on either responds with
    `429 Too Many Requests` or `403 Forbidden`.
    """
    pass
