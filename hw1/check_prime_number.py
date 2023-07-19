"""3. Write code that asks for a number and tells if it's prime or composite.
Use the rule to check: “A number is prime if is only divisible by 1 and itself.
Limit the input of negative numbers and numbers greater than 100 thousand."""
MIN_NUM = 1
MAX_NUM = 100000
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 397, 401, 409, 587, 593, 929, 941]
COMPOSITE = [927, 4, 6, 9]


def is_prime_number(num):
    """ Checks if a number is prime """
    values_k = [x for x in range(2, num + 1)]
    prime = False

    if MIN_NUM < num <= MAX_NUM:
        for k in values_k:
            # n > 1 – prime if there is a remainder when divided by any number
            # other than 1 and n.
            if (k == num) or (num % k != 0):
                prime = True
                continue
            else:
                # composite - if it is divided at least once without a remainder
                prime = False
                break
    else:
        raise ValueError("The number must be greater than 1 but less than or"
                         " equal to 100000")
    return prime


def check_prime(num):
    if is_prime_number(num):
        print(num, "- Prime number")
    else:
        print(num, "- Composite number")


def test():
    print("Test prime and composite numbers")
    print(20 * "=")
    for num in PRIMES + COMPOSITE:
        check_prime(num)
    print(10 * "=", "End of Test", 10 * "=")


if __name__ == '__main__':
    # prime number or composite number
    test()
    try:
        number = int(input("Enter the number: "))

        if number < 0:
            raise ValueError("You entered a negative number")

        check_prime(number)
    except TypeError:
        print("You enter incorrect type data")
    except ValueError as exp:
        print(exp)
