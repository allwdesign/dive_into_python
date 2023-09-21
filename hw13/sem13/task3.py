"""
A module with exception classes. Base exception and child classes -
exceptions: level error, access error.
"""


class MyException(Exception):
    pass


class LevelException(MyException):
    def __str__(self):
        return "User level is lower than your level"


class AccessErrorException(MyException):
    def __str__(self):
        return "No such user"
