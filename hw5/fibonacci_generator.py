from typing import Generator, Any


def fib_gen(num: int) -> Generator[int, Any, None]:
    """Fibonacci number generator function.

    :param num: int
    :return: Generator[int]
    """
    fib_1, fib_2 = 0, 1
    for i in range(num):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        yield fib_1


if __name__ == '__main__':
    for fib_num in fib_gen(8):
        print(fib_num, end=' ')
