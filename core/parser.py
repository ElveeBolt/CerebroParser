from core.filters import *


def is_not_valid(key_values: dict) -> bool:
    if not key_values['phones'] and not key_values['emails']:
        return True

    if not key_values['name']:
        return True


def get_insurance(row):
    insurance = {}

    if row[10]:
        insurance = {
            'title': 'Страховка',
            'country': 'Россия',
            'serial': row[10],
        }
    if insurance and row[11]:
        insurance['authority'] = row[11]

    if insurance:
        return insurance


def get_birth_certificate(row):
    certificate = {}
    if row[12]:
        certificate = {
            'title': 'Свидетельство о рождении',
            'serial': row[12]
        }

    if certificate:
        return certificate


def get_passport(row):
    passport = {}
    if row[13]:
        passport = {
            'title': 'Паспорт',
            'country': 'Россия',
            'serial': row[13],
        }

    if passport and row[14]:
        passport['authority'] = row[14]

    if passport:
        return passport


def get_snils(row):
    snils = {}
    if row[15]:
        snils = {
            'title': 'СНИЛС',
            'country': 'Россия',
            'serial': row[15]
        }

    if snils:
        return snils


def parse_data(row: tuple) -> dict | None:
    insurance = get_insurance(row)
    birt_certificate = get_birth_certificate(row)
    passport = get_passport(row)
    snils = get_snils(row)

    documents = []
    if insurance:
        documents.append(insurance)
    if birt_certificate:
        documents.append(birt_certificate)
    if passport:
        documents.append(passport)
    if snils:
        documents.append(snils)

    if not documents:
        documents = None

    key_values = {
        'name': filter_name(values=[[row[0], row[1], row[2]]]),
        'sex': filter_sex(values=row[4]),
        'birth_date': filter_date(values=row[3], format='%Y-%m-%d %H:%M:%S'),
        'birth_place': row[16],
        'country': filter_country(values=['Россия']),
        'address': filter_address(values=[row[8], row[9]]),
        'phones': filter_phones(values=[row[5], row[6]]),
        'emails': filter_emails(values=[row[7]]),
        'documents': documents,
        'status': filter_status(values=0),
        'category': filter_category(values=0),
        'tags': ['CRM', 'Пациенты']
    }

    if is_not_valid(key_values):
        return

    return {key: value for key, value in key_values.items() if value or value == 0}