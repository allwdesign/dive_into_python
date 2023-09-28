import argparse
import logging
import math

from my_exceptions import NegativeSideLengthError, ZeroSideLengthError

FORMAT = ('{levelname:<8} - {asctime}. В модуле "{name}" в строке '
          '{lineno:03d} функция "{funcName}()" '
          'в {created} секунд записала сообщение: {msg}')

logging.basicConfig(filename='rectangle.log', encoding='utf-8',
                    format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger(__name__)


class Rectangle:
    """
        Class Rectangle.

    >>> r1 = Rectangle(7, 8)
    >>> r2 = Rectangle(5, 6)

    >>> r3 = r1 + r2
    >>> print(r3)
    Rectangle 12 * 8

    >>> r4 = r1 - r2
    >>> print(r4)
    Rectangle 2.0 * 8

    >>> print(r3 == r4)
    False
    >>> print(r3 > r4)
    True
    >>> print(r3 < r4)
    False
    """

    def __init__(self, width, length):
        """The constructor accepts length and width."""

        if width < 0 or length < 0:
            raise NegativeSideLengthError

        if width == 0 or length == 0:
            raise ZeroSideLengthError

        self.w = width
        self.l = length

    def __str__(self):
        """String representation."""
        return f'Rectangle {self.w} * {self.l}'

    def __add__(self, other):
        """Rectangle addition method"""
        return Rectangle(self.w + other.w, self.l)

    def __sub__(self, other):
        """Rectangle subtraction method"""
        return Rectangle(math.fabs(self.w - other.w), self.l)

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
        return round(self.w * self.l, 2)

    def perimeter(self):
        """Method for calculating perimeter."""
        return 2 * (self.w + self.l)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    parser = argparse.ArgumentParser(description='Rectangle parser')
    parser.add_argument('-w1', metavar='width', type=int,
                        help='enter a rectangle width', default=7)
    parser.add_argument('-l1', metavar='length', type=int,
                        help='enter the length of the first rectangle',
                        default=8)
    parser.add_argument('-w2', metavar='width', type=int,
                        help='enter a rectangle width', default=5)
    parser.add_argument('-l2', metavar='length', type=int,
                        help='enter the length of the second rectangle',
                        default=6)

    args = parser.parse_args()

    r1 = Rectangle(args.w1, args.l1)
    logger.info(('Create a rectangle r1={}.\nSquare: {}.\n'
                 'Perimeter: {}.'.format(r1, r1.square(), r1.perimeter())))

    r2 = Rectangle(args.w2, args.l2)
    logger.info(('Create a rectangle r2={}.\nSquare: {}.\n'
                 'Perimeter: {}.'.format(r2, r2.square(), r2.perimeter())))

    r3 = r1 + r2
    logger.info('Rectangle addition method return r3={}'.format(r3))

    r4 = r1 - r2
    logger.info('Rectangle subtraction method return r4={}'.format(r4))

    logger.info('Method compares equality of two rectangles r3={}'
                ' and r4={}: {}'.format(r3, r4, r3 == r4))
    logger.info('r3={} > r4={}: {}'.format(r3, r4, r3 > r4))
    logger.info('r3={} < r4={}: {}'.format(r3, r4, r3 < r4))

    # Must be exceptions
    try:
        r5 = Rectangle(0, 6)
    except ZeroSideLengthError:
        logger.exception(("The lengths of the sides of a rectangle "
                          "cannot be zero"))
    try:
        r5 = Rectangle(44, -6)
    except NegativeSideLengthError:
        logger.exception(("The lengths of the sides of a rectangle "
                          "cannot be negative"))
