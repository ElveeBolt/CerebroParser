from settings import DATA_INDEXES


class Worker:
    """
    Init main worker
    """

    def __init__(self, file: str, delimiter: str, encoding: str, header=False):
        self.file = file
        self.delimiter = delimiter
        self.encoding = encoding
        self.header = header

    def get_tuple(self, row: list | tuple) -> tuple | None:
        """
        Generate tuple with data indices from constant DATA_INDEXES in settings.py

        :param row: list of rows
        :return: list of tuples
        """

        try:
            row = [row[index] for index in DATA_INDEXES]
        except IndexError:
            return

        return tuple(row)
