"""




    4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
import json
from typing import Callable

import my_csv
import roots_finder


def save_result(func) -> Callable:
    """A decorator that saves the passed parameters and the results of

    the function to a json file.

    :return:  Callable.
    """
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@save_result
def save_to_json(data: list) -> None:
    """Save data to json file."""
    print("== Save to json file ==")
    # print("Data", data)
    with open('equation_data.json', 'w') as f:
        json.dump(data, f)


def decorate(func) -> Callable:
    """Decorator that runs the function of finding the roots of a

    quadratic equation with each triple of numbers from the csv file.

    :return: Callable.
    """
    def wrapper(*args):
        return func(*args)
    return wrapper


if __name__ == "__main__":
    data_for_json = []
    numbers = {}

    # Generate data with coefficients and save to csv file
    my_csv.save()

    # Load data with coefficients from csv file without table header
    coefficients_list = my_csv.load()[1:]

    for coefficients in coefficients_list:
        # Convert the coefficient of the quadratic equation
        # to the Fraction type
        numbers = roots_finder.convert(coefficients)
        a = numbers['a']
        b = numbers['b']
        c = numbers['c']

        roots_finder_result = decorate(roots_finder.get_roots)
        result = roots_finder_result(a, b, c)
        # Get roots and print result to the console
        print(f'Coefficients: a: {float(a)}, b: {float(b)},'
              f' c: {float(c)}\n'
              f'{result}')

        # Because Object of type Fraction is not JSON serializable
        for key, val in numbers.items():
            numbers[key] = float(val)

        numbers.update({'result': result})

        data_for_json.append(numbers)

    save_to_json(data_for_json)
