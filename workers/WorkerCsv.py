import csv
from workers.Worker import Worker


class WorkerCsv(Worker):
    """
    csv --> python list

    Worker CSV
    ----------
    This worker parse your csv file to Python list of tuples
    """

    def __init__(self, file: str, delimiter: str, encoding: str, header: bool):
        super().__init__(file, delimiter, encoding, header)

    def read_file(self) -> list:
        with open(file=self.file, mode='r', encoding=self.encoding) as file:
            rows = csv.reader(file, delimiter=self.delimiter)

            if self.header:
                next(rows, None)

            return [self.get_tuple(row) for row in rows if self.get_tuple(row)]

    def run(self) -> list:
        return self.read_file()
