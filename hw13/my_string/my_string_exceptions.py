"""A module with exception classes."""


class OwnerTypeException(Exception):
    """Class OwnerTypeException."""

    def __str__(self):
        return "Owner name must be a type string!"


class ZeroLengthStringError(Exception):
    """Class ZeroLengthStringError."""

    def __str__(self):
        return "The lengths of the string cannot be zero"
