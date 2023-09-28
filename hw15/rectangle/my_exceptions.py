"""A module with exception classes."""


class NegativeSideLengthError(Exception):
    """Class NegativeSideLengthError."""

    def __str__(self):
        return "The lengths of the sides of a rectangle cannot be negative"


class ZeroSideLengthError(Exception):
    """Class ZeroSideLengthError."""

    def __str__(self):
        return "The lengths of the sides of a rectangle cannot be zero"

