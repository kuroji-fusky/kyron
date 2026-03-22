class KyronTable:
    def __init__(self, *,  headings: list[str], data: tuple[list[str], ...]) -> None:
        self.V_SEPARATOR = "|"
        self.H_SEPARATOR = "—"
        self.NOTCH = "+"

        self.parsed_table: list[str] = []

        self._table_def_max_padding: list[tuple[str, int]] = []

        _enumerated_data = enumerate(data, 1)

        # makes sure that all rows have the same number of columns as headings
        for r_index, row in _enumerated_data:
            if len(row) != len(headings):
                raise ValueError(f"Row {r_index} has {len(row)} columns, expected {len(headings)}")  # noqa

        # determining maximum padding
        for h_index, heading in enumerate(headings):
            max_textval = len(heading)

            for r_index, row in _enumerated_data:
                row_text_length = len(row[h_index])

                if max_textval < row_text_length:
                    max_textval = row_text_length

                # push whatever max value if it's the last value in list
                if r_index == len(data):
                    self._table_def_max_padding.append((heading, max_textval))  # noqa

        # adds heading to stdout
        t_heading = self._pad_lists(headings)

        t_separator_partial = [
            self._pad_value(self.H_SEPARATOR, pad=p+2)
            for _, p in self._table_def_max_padding
        ]
        t_separator: str = self._wrap_row(self.NOTCH, self.NOTCH.join(t_separator_partial))  # noqa

        self.parsed_table.extend([t_separator, t_heading, t_separator])  # noqa

        # adds the table content afterwards
        for content_row in data:
            self.parsed_table.append(self._pad_lists(content_row))

        self.parsed_table.append(t_separator)

    def display(self):
        return "\n".join(self.parsed_table)

    def _pad_lists(self, lists: list[str]):
        max_len = [l for _, l in self._table_def_max_padding]  # noqa

        zipped_padding = zip(lists, max_len)
        return self._wrap_row(self.V_SEPARATOR, [f" {text.ljust(ext_padding)} "
                                                 for text, ext_padding in zipped_padding])

    def _wrap_row(self, wrapper: str, dyn_item: list[str] | str):
        """Consolidates data into a table row

        Args:
            wrapper (str): a char wrapper for both starting and ending string
            dyn_item (list[str] | str): items for a certain data point

        Returns:
            string: lmao
        """
        _templ = "{}{}{}"

        if isinstance(dyn_item, str):
            return _templ.format(wrapper, dyn_item, wrapper)

        if isinstance(dyn_item, list):
            return _templ.format(wrapper, self.V_SEPARATOR.join(dyn_item), wrapper)

    @staticmethod
    def _pad_value(fillchar: str = "", *, pad=12):
        return fillchar * pad
