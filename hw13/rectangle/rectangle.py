import math

from my_rectanle_exceptions import NegativeSideLengthError


class Rectangle:
    """Class Rectangle."""

    def __init__(self, a, b):
        """The constructor accepts length and width."""
        if a < 0 or b < 0:
            raise NegativeSideLengthError
        if a == 0 or b == 0:
            raise ZeroSideLengthError
        self.w = a
        self.h = b

    def __str__(self):
        """String representation."""
        return f'Rectangle {self.w} * {self.h}'

    def __add__(self, other):
        """Rectangle addition method"""
        return Rectangle(self.w + other.w, self.h)

    def __sub__(self, other):
        """Rectangle subtraction method"""
        return Rectangle(math.fabs(self.w - other.w), self.h)

    def __eq__(self, other):
        """Method compares two rectangles."""
        return self.square() == other.square()

    def __gt__(self, other):
        """Method(greate than) compares rectangle squares."""
        return self.square() > other.square()

    def __lt__(self, other):
        """Method(less than) compares rectangle squares."""
        return self.square() < other.square()

    def square(self):
        """Method for calculating area."""
        return round(self.w * self.h, 2)

    def perimeter(self):
        """Method for calculating perimeter."""
        return 2 * (self.w + self.h)


if __name__ == '__main__':
    r1 = Rectangle(7, 8)
    r2 = Rectangle(5, 6)

    r3 = r1 + r2
    print(r3)

    r4 = r1 - r2
    print(r4)

    print('Equal:', r3 == r4)
    print('r3 > r4:', r3 > r4)
    print('r3 < r4:', r3 < r4)
