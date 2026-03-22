from ..platform_checks import IS_LINUX, IS_MACOS, IS_WINDOWS
import abc


class _KyronSchedulerBase(abc.ABC):
    def assign_task(self, name: str):
        ...

    @abc.abstractmethod
    def list_tasks(self):
        pass

    @abc.abstractmethod
    def remove(self, id: str):
        pass

    @abc.abstractmethod
    def change(self, id: str):
        pass

    @abc.abstractmethod
    def add(self, id: str):
        pass


class WindowsScheduler(_KyronSchedulerBase):
    def __init__(self):
        super().__init__()


class LinuxScheduler(_KyronSchedulerBase):
    def __init__(self):
        super().__init__()


class RichBoiScheduler(_KyronSchedulerBase):
    def __init__(self):
        super().__init__()


def schduler() -> _KyronSchedulerBase | NotImplementedError:
    if IS_WINDOWS:
        return WindowsScheduler()

    if IS_LINUX:
        return LinuxScheduler()

    if IS_MACOS:
        return RichBoiScheduler()

    return NotImplementedError("Bruh.")
