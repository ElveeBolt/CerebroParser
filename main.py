from settings import *
from core import core, parser
from workers.WorkerTxt import WorkerTxt
from workers.WorkerCsv import WorkerCsv


def main():
    db = core.create_db()
    file_extension = core.get_file_extension(path=FILE_PATH)

    print(f'Start file {file_extension} parse...')
    match file_extension:
        case 'txt':
            worker = WorkerTxt(file=FILE_PATH, encoding=FILE_ENCODING, delimiter=DELIMITER, header=HEADER)
        case 'csv':
            worker = WorkerCsv(file=FILE_PATH, encoding=FILE_ENCODING, delimiter=DELIMITER, header=HEADER)
        case _:
            return print('This format is not supported')

    rows = worker.run()
    unique = core.get_unique(rows)
    counts = core.get_count(rows=rows, unique=unique)

    index, i = 0, 0
    items = []
    collection = core.generate_collection_name(index=index)

    for row in unique:
        item = parser.parse_data(row)

        if not item:
            continue

        if i % COLLECTION_SIZE == 0:
            collection = core.generate_collection_name(index=index)
            db.create_collection(collection)
            print(f'Create collection - {collection}')
            index += 1

        i += 1
        items.append(item)

        if i % INSERT_COUNT == 0:
            db[collection].insert_many(items)
            items = []

    if items:
        db[collection].insert_many(items)

    core.print_result(counts=counts, i=i, index=index)


if __name__ == '__main__':
    main()