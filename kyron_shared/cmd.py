from typing import Any
import json
import re
import shutil


ArgValue = str | int | float | bool | dict[str, Any]


class KyronCommandScaffolder:
    """Scaffolds commands in a programmatic way; wraps `subprocess` and `os`"""

    def __init__(self, base_exec: str, *,
                 precheck: bool = True) -> None:
        """
        Args:
            base_exec (str): The program what will be executed along with its arguments it'll be passed through.
            precheck (bool, optional): Ensures that the executable provided exists. Defaults to True.
        """
        self.base_exec = base_exec
        self._parsed_cli_args: list[ArgValue] = [base_exec]

        if precheck:
            exec = KyronCommandScaffolder.detect_exec(base_exec)

            if exec is None:
                raise FileNotFoundError(f"Executable {base_exec} does not exist")  # noqa

    @staticmethod
    def detect_exec(exec: str):
        """A wrapper for `shutil.which` that returns an executable, will return `None` otherwise"""
        exec_path = shutil.which(exec)

        if exec_path is not None:
            return exec_path

        return None

    def add_argument[ArgType: ArgValue = str](self, arg_name: str, arg_value: ArgType, *, parse_json=False):
        """Appends an argument

        Args:
            arg_name (str): Argument name, beginning with `-` or `--`
            arg_value (str | int | float | bool): Argument value, could either be string, number, or a boolean value
            parse_json (bool, optional): If argument value is a dictionary/object, auto-parse as JSON string. Defaults to False.

        Raises:
            ArgumentError: If either argument names and value aren't provided
        """
        if is_string_falsy(arg_name) or is_string_falsy(str(arg_value)):
            raise ArgumentError("No arguments provided")

        if not re.match(r"^(/|-{1,2}|\+)", arg_name):
            raise ArgumentError("Invalid argument key. An argument name must begin with dashes (`-`, `--`), "
                                "a plus sign (`+`), or a slash (`/`) on Windows.")

        if parse_json and isinstance(arg_value, dict):
            json_value = json.dumps(arg_value)

            self._parsed_cli_args.extend([arg_name, json_value])
            return

        self._parsed_cli_args.extend([arg_name, str(arg_value)])

    def add_positional_argument[ArgType: ArgValue = str](self, pos_arg_value: ArgType, *, autostrip=False):
        """Appends a positional argument

        Args:
            arg (str | int | bool): Argument value
            autostrip (bool, optional): If value type is string, it automatically strips any whitespace, treating it as a sub-command in specific command line applications. Defaults to `False`.
        """
        if autostrip and isinstance(pos_arg_value, str):
            # split string then strip on the empty ones
            sanitized_out = re.split(r"\s+", pos_arg_value)

            self._parsed_cli_args.extend(sanitized_out)
            return

        self._parsed_cli_args.extend([str(pos_arg_value)])

    def output(self):
        return " ".join(str(value) for value in self._parsed_cli_args)


def is_string_falsy(s: str) -> bool:
    if not isinstance(s, str):
        return False

    return not s or not s.strip()


class ArgumentError(Exception):
    pass
