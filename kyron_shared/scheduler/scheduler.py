from ..platform import is_windows, is_linux, is_macos
import abc
from typing import final, Literal, Optional

__all__ = ["scheduler"]


class _OSNativeScheduler(abc.ABC):
    @abc.abstractmethod
    def list_tasks(self):
        pass

    @abc.abstractmethod
    def remove_task(self, id: str):
        pass

    @abc.abstractmethod
    def change_task(self, id: str):
        pass

    @abc.abstractmethod
    def add_task(self, id: str):
        pass


@final
class WindowsScheduler(_OSNativeScheduler):
    def __init__(self):
        super().__init__()

    def remove_task(self, id: str):
        ...

    def add_task(self, id: str):
        ...

    def change_task(self, id: str):
        ...

    def list_tasks(self):
        ...


_LinuxSchedulerMode = Literal["systemd", "crontab"]


@final
class LinuxScheduler(_OSNativeScheduler):
    def __init__(self, scheduler: Optional[_LinuxSchedulerMode] = "crontab"):
        super().__init__()

        # check the init system supports either systemd timers or cron
        # so it'll properly route the proper scheduler, user might choose to override them
        # but it'll fallback to crontab if any errors occurs
        self.__scheduler_mode = scheduler

    def __use_systemd_timers(self):
        ...

    def __use_crontab(self):
        ...

    def remove_task(self, id: str):
        ...

    def add_task(self, id: str):
        ...

    def change_task(self, id: str):
        ...

    def list_tasks(self):
        ...


@final
class MacOSScheduler(_OSNativeScheduler):
    def __init__(self):
        super().__init__()

    def remove_task(self, id: str):
        ...

    def add_task(self, id: str):
        ...

    def change_task(self, id: str):
        ...

    def list_tasks(self):
        ...


def scheduler() -> _OSNativeScheduler | OSError:
    if is_windows:
        return WindowsScheduler()

    if is_linux:
        return LinuxScheduler()

    if is_macos:
        return MacOSScheduler()

    return OSError("Operating system not supported, bruh.")
