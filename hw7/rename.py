"""This module for bulk renaming of files.

"""
import os

from tests import create_test_files, del_test_files


def rename(*, wanted_name: str = '', count_nums: int,
           extension_old: str, extension_new: str,
           diapazon: list[int]) -> None:
    """Bulk file renaming function.

    :param wanted_name: str. The desired final file name. When renaming,
        a sequence number is added to the end of the name.
    :param count_nums: int. The number of digits in the sequence number.
    :param extension_old: str. The extension of the source file.
        Renaming should only work for these files inside the directory.
    :param extension_new: str. The extension of the destination file.
    :param diapazon: list[int]. The range of the original name to be
        stored. For example, for the range [3, 6], letters 3 through 6
        are taken from the original file name. To these is added the
        desired final name, if it is passed.
        Next, the file counter and extension.
    :return: None.
    """
    need_rename = []
    start, stop = diapazon
    for obj in os.listdir():
        if os.path.isfile(obj) and obj.endswith(extension_old):
            need_rename.append(obj)

    for idx, old_name in enumerate(need_rename, start=1):
        # helper.py -> ['helper', '']
        b_old_name = os.path.basename(old_name).split(extension_old)[0]
        new_name = (f"{b_old_name[start:stop]}{wanted_name}"
                    f"{str(idx).zfill(count_nums)}{extension_new}")

        os.rename(os.path.join(os.getcwd(), old_name),
                  os.path.join(os.getcwd(), new_name))


if __name__ == '__main__':
    path = os.getcwd()
    create_test_files(path, ['txt', 'csv', 'png'])
    rename(wanted_name="video", count_nums=3, extension_old=".txt",
           extension_new=".csv", diapazon=[3, 6])
    del_test_files(path, ['csv', 'png'])
