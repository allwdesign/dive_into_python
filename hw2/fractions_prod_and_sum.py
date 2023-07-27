from fractions import Fraction
import math

SEPARATOR = "/"

try:

    first_string = input("Enter first fraction: ")
    second_string = input("Enter second fraction: ")

    first_fraction_values = first_string.split(SEPARATOR)
    second_fraction_values = second_string.split(SEPARATOR)

    if (first_fraction_values[1] == "0") or (second_fraction_values[1] == "0"):
        raise ArithmeticError("Divide by zero is not allowed")

    first_numerator = int(first_fraction_values[0])
    second_numerator = int(second_fraction_values[0])
    first_denominator = int(first_fraction_values[1])
    second_denominator = int(second_fraction_values[1])

    print(f'Product: {first_numerator * second_numerator}/'
          f'{first_denominator * second_denominator}')

    if first_denominator == second_denominator:
        sum_frs = first_numerator + second_numerator
        print(f'Sum: {first_numerator + second_numerator}/{first_denominator}')
    else:
        f_lcm = math.lcm(first_denominator, second_denominator)

        a = ((f_lcm / first_denominator) * first_numerator) + \
            ((f_lcm / second_denominator) * second_numerator)
        print(f'Sum: {int(a)}/{f_lcm}')

    print("Check with fractions module")
    sum = Fraction(first_string) + Fraction(second_string)
    print(f'Answer for sum: {sum}')
    prod = Fraction(first_string) * Fraction(second_string)
    print(f'Answer for prod: {prod}')

except ArithmeticError as exp:
    print(exp)
except TypeError:
    print("You enter incorrect type data")
except ValueError as exp:
    print(exp)
