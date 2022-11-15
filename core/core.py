import os
from pymongo import MongoClient
from settings import *


def get_file_extension(path: str) -> str:
    """
    Extracting extension from filename in Python

    :param path: string of file path
    :return: string of extension
    """

    filename, file_extension = os.path.splitext(path)
    return file_extension.split('.')[-1]


def get_unique(rows: list) -> list:
    """
    Get unique values from list

    :param rows: list of rows
    :return: list of unique values
    """
    return set(rows)


def get_count(rows: list, unique: list) -> dict:
    """
    Get count items in all and unique rows

    :param rows: list of all rows
    :param unique: list of unique rows
    :return: dict of counts item in parameters
    """
    len_rows = len(rows)
    len_unique = len(unique)
    len_drop = len_rows - len_unique
    return {'all': len_rows, 'unique': len_unique, 'drop': len_drop}


def print_result(counts: dict, i: int, index: int) -> None:
    """
    Print result work script

    :param counts: list of main count items
    :param i: items added
    :param index: count created collections
    :return: print result
    """
    return print(f'\nFinished:\n'
                 f'{counts["all"]} - all items\n'
                 f'{counts["unique"]} - unique items\n'
                 f'{counts["drop"]} - droped (duplicates) items\n'
                 f'{counts["unique"] - i} - filtered items\n'
                 f'{i} - items added (correct items)\n'
                 f'{index} - collections created')


def generate_collection_name(index: int) -> str:
    """
    This function get collection name from
    settings.py and add index to this name

    :param index:
    :return: collection name
    """
    return COLLECTION_NAME + str(index)


def create_db():
    """
    Connect to MongoClient with HOST and PORT from settings.py
    Create database with name from settings.py

    :return: connection to database
    """
    client = MongoClient(host=HOST, port=PORT)
    return client[DATABASE]