from typing import Iterable, Sequence, Mapping, Any, Union, cast


class KyronTable:
    def __init__(self,
                 *,
                 headings: list[str],
                 data: Iterable[Union[Sequence[Any], Mapping[str, Any]]],
                 columns: list[str] | None = None):
        self.V_SEPARATOR = "|"
        self.H_SEPARATOR = "—"
        self.CORNER = "+"

        self.parsed_table: list[str] = []

        self._table_def_max_padding: list[tuple[str, int]] = []

        # materialize data to allow multiple passes
        rows_list = list(data)

        # convert to sequences if rows are mappings
        if rows_list and isinstance(rows_list[0], Mapping):
            if columns is None:
                first_keys = rows_list[0].keys()
                if all(h in first_keys for h in headings):
                    columns = list(headings)
                    display_headings = list(headings)
                else:
                    raise ValueError("When passing mapping rows, you must provide `columns` mapping or use headings that match mapping keys")  # noqa
            else:
                display_headings = list(headings)

            data_rows: list[list[str]] = []
            for row in rows_list:
                row_seq = [str(cast(Mapping[str, Any], row).get(col, ""))
                           for col in columns]
                data_rows.append(row_seq)
        else:
            # assume rows are sequences; coerce items to str
            data_rows = [list(map(lambda v: "" if v is None else str(v), row))
                         for row in rows_list]
            display_headings = list(headings)

        # makes sure that all rows have the same number of columns as headings
        for r_index, row in enumerate(data_rows, 1):
            if len(row) != len(display_headings):
                raise ValueError(f"Row {r_index} has {len(row)} columns, expected {len(display_headings)}")  # noqa

        # determining maximum padding
        for h_index, heading in enumerate(display_headings):
            max_textval = len(heading)

            # padding must match heading length
            if not data_rows:
                self._table_def_max_padding.append((heading, max_textval))
                continue

            for r_index, row in enumerate(data_rows, 1):
                row_text_length = len(row[h_index])

                if max_textval < row_text_length:
                    max_textval = row_text_length

                # push whatever max value if it's the last value in list
                if r_index == len(data_rows):
                    self._table_def_max_padding.append((heading, max_textval))  # noqa

        # adds heading to stdout, use display_headings for rendered labels
        t_heading = self._pad_lists(display_headings)

        t_separator_partial = [self._pad_value(self.H_SEPARATOR, pad=p+2)
                               for _, p in self._table_def_max_padding]

        t_separator = self._wrap_row(self.CORNER, self.CORNER.join(t_separator_partial))  # noqa

        self.parsed_table.extend([t_separator, t_heading, t_separator])  # noqa

        # adds the table content afterwards
        for content_row in data_rows:
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
