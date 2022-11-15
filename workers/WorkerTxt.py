from workers.Worker import Worker


class WorkerTxt(Worker):
    """
    txt --> python list

    Worker TXT
    ----------
    This worker parse your txt file to Python list of tuples
    """
    def __init__(self, file: str, delimiter: str, encoding: str, header: bool):
        super().__init__(file, delimiter, encoding, header)

    def read_file(self) -> list:
        with open(file=self.file, mode='r', encoding=self.encoding, errors='ignore') as file:

            if self.header:
                next(file, None)

            return [row.rstrip() for row in file]

    def parse_data(self, data: list) -> list:
        list = []
        for row in data:
            row = row.split(self.delimiter)
            if self.get_tuple(row):
                list.append(self.get_tuple(row))

        return list

    def run(self) -> list:
        data = self.read_file()
        return self.parse_data(data)

