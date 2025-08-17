"""Utils for dealing with filesystems"""

size = {
    "KB": 1024 ** 1,
    "MB": 1024 ** 2,
    "GB": 1024 ** 3,
    "TB": 1024 ** 4,
}

size_tupled = [(c, s) for c, s in size.items()]


def calculate_disk_space(raw_byte_count: int):
    def _round_by_byte(_id: tuple[str, int]):
        # hah, byte size lol
        [capacity, byte_size] = _id

        return f"{round(raw_byte_count / byte_size, 2)} {capacity}"

    if raw_byte_count < size["KB"]:
        return f"{raw_byte_count} B"
    elif raw_byte_count < size["MB"]:
        return _round_by_byte(size_tupled[0])
    elif raw_byte_count < size["GB"]:
        return _round_by_byte(size_tupled[1])
    elif raw_byte_count < size["TB"]:
        return _round_by_byte(size_tupled[2])

    # terabytes is the higher limit for this project
    elif raw_byte_count >= size["TB"]:
        return _round_by_byte(size_tupled[3])
    else:
        return "Unknown"
