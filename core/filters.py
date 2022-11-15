import re
import string
from settings import *
from datetime import datetime


def filter_name(values: list) -> list | None:
    """
    Filter for name

    - Check if name is empty
    - Delete start and end spaces
    - Format from "sergio ramos" to "Sergio Ramos"
    :param values: list of names
    :return: filtered list or None
    """

    list = []
    for names in values:
        name_list = []
        if not names:
            continue

        for name in names:
            name = name.strip()
            name = string.capwords(name)
            if name:
                name_list.append(name)

        if name_list:
            strings = ' '.join(name_list)
            list.append(strings)

    if list:
        return list


def filter_sex(values: str) -> int | None:
    """
    Filter for sex

    - Check if sex is empty
    - Delete start and end spaces
    - Format string to lowercase
    :param values: string of sex
    :return: filtered int or None
    """

    if not values:
        return

    values = values.strip().lower()
    for key, value in FILTER_SEX.items():
        if values in value:
            return key


def filter_date(values: str, format: str) -> str | None:
    """
    Filter for date

    - Check if date is empty
    - Delete start and end spaces
    - Format date to
    :param values: string of date
    :param format
    :return: filtered date or None
    """

    if not values:
        return

    values = values.strip()
    date = datetime.strptime(values, format)

    return datetime.strftime(date, '%d.%m.%Y')


def filter_country(values: list) -> str | None:
    """
    Filter for country

    - Delete start and end spaces
    - Format from "poland" to "Poland"
    :param values: list of countries
    :return: filtered string or None
    """

    list = []
    for value in values:
        if not value:
            continue
        value = value.strip().title()
        list.append(value)

    if list:
        return ' '.join(list)


def filter_address(values: list) -> str | None:
    """
    Filter for address

    - Delete start and end spaces,
    - Replace and check reduction of streets from settings.py
    :param values: list of addresses
    :return: filtered string or None
    """

    list = []
    for value in values:
        if not value:
            continue
        value = value.split(' ')
        print(value)
        correct_value = []

        for text in value:
            for key, val in FILTER_ADDRESSES.items():
                if text.lower() in val:
                    text = key

            correct_value.append(text)


        list.append(' '.join(correct_value))

    if list:
        return ', '.join(list)


def filter_phones(values: list) -> list | None:
    """
    Filter for phones

    - Delete start and end spaces
    - Remove all non-numeric characters from string
    :param values: list of phones
    :return: filtered list or None
    """

    list = []
    for value in values:
        if not value:
            continue
        value = value.strip()
        value = re.sub('[^0-9]', '', value)
        if value:
            list.append(value)

    if list:
        return list


def filter_emails(values: list) -> list | None:
    """
    Filter for emails

    - Delete start and end space
    - Check valid email
    - All symbols to lowercase
    :param values: list of emails
    :return: filtered list or None
    """

    regex = r'\b[a-z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,}\b'

    list = []
    for value in values:
        if not value:
            continue

        value = value.strip().lower()

        if re.fullmatch(regex, value):
            list.append(value)

    if list:
        return list


def filter_comment(values: str) -> str | None:
    """
    Filter for comment

    - Delete start and end spaces
    :param values: string of comments
    :return: filtered str or None
    """
    if values:
        return values.strip()


def filter_ip(values: list) -> list | None:
    """
    Filter for ip

    - Delete start and end spaces
    :param values: string of ip
    :return: filtered string or None
    """

    list = []
    for value in values:
        if not value:
            continue
        value = value.strip()
        list.append(value)

    if list:
        return list


def filter_coordinates(values: list) -> list | None:
    """
    Filter for coordinates

    - Delete start and end spaces
    :param values: string of coourdinates
    :return: filtered string or None
    """

    list = []
    for value in values:
        if not value:
            continue
        value = value.strip()
        list.append(value)

    if list:
        return list


def filter_category(values: int) -> int | None:
    """
    Filter for category

    :param values: int of category
    :return: filtered int
    """

    if values:
        return values


def filter_status(values: int) -> int | None:
    """
    Filter for status

    :param values: status
    :return: filtered int
    """

    if values:
        return values
