class kyron_logger:
    def __init__(self, *, verbose_mode=False) -> None:
        self._verbose_mode = verbose_mode

    def debug(self, *a):
        if not self._verbose_mode:
            return

        print("[VERBOSE]", *a)

    @staticmethod
    def info(*a):
        print("[INFO]", *a)
