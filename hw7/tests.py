"""Сontains functions for creating and deleting test files.

"""
import os


def create_test_files(parent_dir: str, extentions: list[str]) -> None:
    """Create files for test.

    :param parent_dir: str. String with absolute path for current dir.
    :param extentions: list[str]. List with extensions for test files.
    :return: None.
    """
    for ext in extentions:
        for i in range(3):
            new_filename = f'file_{i}.{ext}'
            with open(os.path.join(parent_dir, new_filename), 'a') as f:
                pass


def del_test_files(parent_dir: str, extentions: list[str]) -> None:
    """Delete test files.

    :param parent_dir: str. String with absolute path for current dir.
    :param extentions: list[str]. List with extensions for test files.
    :return: None.
    """
    for ext in extentions:
        for obj in os.listdir(parent_dir):
            if os.path.isfile(obj) and obj.endswith(ext):
                os.remove(os.path.join(parent_dir, obj))
