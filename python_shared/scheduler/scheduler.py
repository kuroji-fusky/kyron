from ..platform_checks import IS_LINUX, IS_MACOS, IS_WINDOWS  # type: ignore
import abc
from typing import final, Literal, Optional


class _OSNativeScheduler(abc.ABC):
    # def assign_task(self, name: str):
    #     ...

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
    if IS_WINDOWS:
        return WindowsScheduler()

    if IS_LINUX:
        return LinuxScheduler()

    if IS_MACOS:
        return MacOSScheduler()

    return OSError("Bruh.")


__all__ = ["scheduler"]