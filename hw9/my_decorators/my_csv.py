import csv
import random
from typing import Generator


def generate_data() -> Generator:
    """
    2. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    :return:
    """
    for i in range(100, 1001):
        yield {'a': random.uniform(-100, 101),
               'b': random.uniform(-100, 101),
               'c': random.uniform(-100, 101)}


def save() -> None:
    """Save data to csv file."""
    print("== Save to csv file ==")
    with open('coefficients.csv', 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['a', 'b', 'c'],
                                   dialect='excel',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        for data in generate_data():
            csv_write.writerow(data)


def load() -> list[dict]:
    """Load data from csv file."""
    print("== Load data from csv file ==")
    data = []
    with open('coefficients.csv', 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.DictReader(f, fieldnames=['a', 'b', 'c'],
                                  dialect='excel',
                                  quoting=csv.QUOTE_NONNUMERIC)
        for line in csv_file:
            data.append({'a': line['a'], 'b': line['b'], 'c': line['c']})
    return data
