"""
This program will find the roots of a quadratic equation.

Example: 6*x^2+5*x+6=0.
"""
import re
from fractions import Fraction

POSITIVE_ONE = '+'
NEGATIVE_ONE = '-'
FIRST_ROOT = 'First root: x ='
SECOND_ROOT = 'Second root: x ='


def get_roots(a: Fraction, b: Fraction, c: Fraction) -> str:
    """
    Calculates the roots of a quadratic equation. The result rounds up to two
    decimal places.

    Full quadratic equation: a*x^2+b*x+c=0, where a!=0.
    Incomplete quadratic equation:
    1. a*x^2+b*x=0, where a!=0, b!=0, c=0
    2. a*x^2+c=0,   where a!=0, b=0,  c!=0.

    :param a: Fraction. Coefficient of a quadratic equation.
        Example: Fraction(6, 1)
    :param b: Fraction. Coefficient of a quadratic equation.
        Example: Fraction(5, 1)
    :param c: Fraction. Coefficient of a quadratic equation.
        Example: Fraction(6, 1)
    :return: str. String with result.
    """
    try:
        roots_msg = ""

        if b != 0 and c != 0:
            # a*x^2+b*x+c=0. Examples: 6*x^2+5*x+6=0  or -6*x^2-5*x-6=0.
            d = b ** 2 - 4 * a * c
            if d > 0:
                # Two roots
                x1 = float((-b + d ** 0.5) / (2 * a))
                x2 = float((-b - d ** 0.5) / (2 * a))
                roots_msg = f'{FIRST_ROOT} {x1:.2f}. {SECOND_ROOT} {x2:.2f}.'
            elif d < 0:
                roots_msg = "No real roots!"
            else:
                # d=0
                x1 = float(-(b / (2 * a)))
                roots_msg = f"Two equal roots: x = {x1:.2f}."
        elif b == 0 and c == 0:
            # a*x^2=0. Example: 10*x^2=0.
            roots_msg = "One root: x = 0."
        elif c == 0:
            # a*x^2+b*x=0. Example: 6*x^2+5*x=0.
            x2 = float(- b / a)
            roots_msg = f'{FIRST_ROOT} 0. {SECOND_ROOT} {x2:.2f}.'
        else:
            # b=0, a*x^2+c=0. Example: x^2 + 5= 0.
            if -c / a > 0:
                x1 = float((-c / a) ** 0.5)
                x2 = float(-((-c / a) ** 0.5))
                roots_msg = f'{FIRST_ROOT} {x1:.2f}. {SECOND_ROOT} {x2:.2f}.'
            else:
                # -c / a < 0
                roots_msg = "No solutions!"

        return roots_msg
    except ZeroDivisionError as e:
        raise ZeroDivisionError('Error: Division by zero! ')


def convert(coefficients: dict) -> dict:
    """
    Convert the coefficient of the quadratic equation to the Fraction type

    Full quadratic equation: a*x^2+b*x+c=0, where a!=0.
    Incomplete quadratic equation:
    1. a*x^2+b*x=0, where a!=0, b!=0, c=0
    2. a*x^2+c=0,   where a!=0, b=0,  c!=0.

    a,b,c - coefficients of quadratic equation.
    a -> coefficients['a']
    b -> coefficients['b']
    c -> coefficients['c']

    The coefficient standing before x equal to one is omitted when writing.
    Examples:
    if x^2+x=0, then a='' and b='+' it means a=1 and b=1
    if -x^2-x=0, then a=b='-' it means a=b=-1
    b=c=None - it means b=с=0

    :param coefficients: dict.
        Example: {'a': '6', 'b': '+5', 'c': '+6'}
    :return: dict.
        Example:
            {'a': Fraction(6, 1), 'b': Fraction(5, 1), 'c': Fraction(6, 1)}
    """
    coef = None
    nums = dict()

    for key, val in coefficients.items():
        if ((key == 'a' and not val)
                or (key == 'b' and val == POSITIVE_ONE)):
            # a='' or b='+'
            coef = Fraction(1)
        elif not val:
            # b=c='' or None
            coef = Fraction(0)
        elif val == NEGATIVE_ONE:
            # a=b='-'
            coef = Fraction(-1)
        else:
            # If a,b,c > 0  or a,b,c < 0
            coef = Fraction(val)

        nums[key] = coef

    return nums

