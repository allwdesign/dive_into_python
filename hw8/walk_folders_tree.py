"""The module contains functions for recursively traversing the
directory tree and calculating the size of directories and files.
"""
import os
from typing import Iterator

import my_csv
import my_json
import my_pickle

MODULE_NAMES = ['json', 'csv', 'pickle']


def get_dir_size(path: str) -> int:
    """Function for calculating the dir size in bytes.

    :param path: String representation for dir path.
    :return: int.
    """
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def get_size(path: str, item_type: str) -> int:
    """Function for calculating the object size in bytes.

    For directories, the size is calculated taking into account all
    nested files and directories.

    :param path: str. String representation for file or dir path.
    :param item_type: str.
    :return: int.
    """
    size = os.path.getsize(path)
    if item_type == 'dir':
        size = get_dir_size(path)
    return size


def get_items(items: list[str], parent: str, item_type: str) -> list[dict]:
    """This function creates a list of dictionaries with properties of
    the specified objects.

    :param items: list[str]. List with filenames or dirnames.
    :param parent: str. Parent dir.
    :param item_type: str['file'|'dir'].
    :return: list[dict]. List of dictionaries with object properties.
    """
    data = []

    for item in items:
        path = os.path.join(parent, item)
        item_dict = {
            "name": item,
            "parent": parent,
            "type": item_type,
            'size': get_size(path, item_type)
        }

        data.append(item_dict)

    return data


def prepare_data_for_saving(data: Iterator[tuple]) -> list[dict]:
    """This function prepare data for saving.

    :param data: Iterator[tuple]. Data obtained when traversing the
        directory tree.
    :return: list[dict].
    """
    all_data = []

    for address, sub_dirs, files in data:
        sub_dirs_properties = get_items(sub_dirs, address, "dir")
        files_properties = get_items(files, address, "file")
        all_data.extend(sub_dirs_properties)
        all_data.extend(files_properties)

    return all_data


def recursive_walk(dir_name) -> Iterator[tuple]:
    """

    :param dir_name:
    :return: Iterator[tuple]
    """
    try:
        os.chdir(dir_name)
    except OSError as e:
        print(e)

    return os.walk(dir_name)


def save(data) -> None:
    """The function for saving data in the specified format.

    :param data: Data for saving in the specified format.
    :return: None.
    """
    for modulename in MODULE_NAMES:
        globals()['my_' + modulename].save(data)


def load() -> None:
    """The function for loading data from file.

    :return: None.
    """
    for modulename in MODULE_NAMES:
        globals()['my_' + modulename].load()


if __name__ == '__main__':
    path = os.getcwd()
    tree = prepare_data_for_saving(recursive_walk(path))
    save(tree)
    load()
