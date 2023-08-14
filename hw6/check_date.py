"""Module for checking date.

It is possible to run in the terminal with the date for verification.
"""
import re
from sys import argv


FEBRUARY = 2
LEAP_YEAR_FEBRUARY_DAYS = 29
DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def check_date_exist(date_string: str) -> bool:
    """Checks if a date exists.

    The year can be in the range [1, 9999]. The entire period
    (January 1, 1 - December 31, 9999) is valid for the Gregorian
    calendar.

    :param date_string: str. Date string in format DD.MM.YYYY
    :return: bool. True if the date can exist or False.
    """
    result = False

    # Exceptions split
    day, month, year = list(map(int, date_string.split('.')))
    print(day, month, year)

    if year in range(1, 10_000):
        if month in DAYS_IN_MONTH:
            last_day = DAYS_IN_MONTH[month]
            if month == FEBRUARY and _is_leap_year(year):
                # 29 days in feb
                last_day = LEAP_YEAR_FEBRUARY_DAYS
            if day in range(1, last_day + 1):
                return True
    return result


def _is_leap_year(year: int) -> bool:
    """Checking the year for leap years.

    :param year: int
    :return: bool
    """
    leap_year = False

    if year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
        leap_year = True

    return leap_year


if __name__ == '__main__':
    if "-d" in argv and len(argv) == 3:
        user_date_string = argv[-1]
    else:
        print("ARGV", argv)
        user_date_string = input("Enter your date in format DD.MM.YYYY: ")

    try:
        if re.fullmatch(r'\d{2}.\d{2}.\d{4}', user_date_string) is None:
            raise ValueError("Incorrect format for date")

        if check_date_exist(user_date_string):
            msg = "Date exist"
        else:
            msg = "Date not exist"

        print(msg)
    except ValueError as er:
        print(er)


