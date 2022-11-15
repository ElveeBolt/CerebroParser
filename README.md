# 💎 CerebroParser
[![Supported python versions](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/downloads/)
[![First repository](https://img.shields.io/badge/GitHub-First%20repository-brightgreen)](https://github.com/ElveeBolt/CerebroParser)

Installation guide for CerebroParser.


Supported file extensions: <kbd>TXT</kbd>, <kbd>CSV</kbd>

## Installing CerebroParser
```bash
git clone https://github.com/ElveeBolt/CerebroParser.git
cd CerebroParser
```

### Linux / Ubuntu
```bash
python3 -m venv venv
source venv\bin\activate
pip install -r requirements.txt
```

### Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Configurate
First you must rename <kbd>settings_conf.py</kbd> to <kbd>settings.py</kbd> and check settings in this files

```python
# Mongo settings
HOST = 'mongodb://127.0.0.1'
PORT = 27017
```

```python
# File Database
FILE_PATH = 'database/database.csv' # path to your database file
FILE_ENCODING = 'utf-8' # encoding your data
HEADER = True # if your file have header use True.
DELIMITER = ';' # delimiter your data in rows
DATA_INDEXES = [0, 1, 2, 3, 4] # indices of columns your file
```

```python
# Database settings
DATABASE = 'Database' # database name
COLLECTION = 'collection_' # collection names
COLLECTION_SIZE = 5000000 # collection size
INSERT_COUNT = 10000 # we use 'Insert many'. You can config size items in package
```

## Ready to use
```bash
python main.py
```