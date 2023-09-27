"""Module for testing Matrices with pytest."""

import pytest

from hw11.my_matrix import Matrix


@pytest.fixture
def multiply_data():
    return (Matrix([[3, 6, 7], [5, -3, 0]]),
            Matrix([[1, 1], [2, 1], [3, -3]]),
            Matrix([[36, -12], [-1, 2]]))


@pytest.fixture
def addition_data():
    return Matrix([[2, 4], [5, -6]]), Matrix([[9, -3], [3, 6]])


def test_multiply(multiply_data):
    m1, m2, mul_result = multiply_data

    assert m1 * m2 == mul_result


def test_addition_method(addition_data):
    m1, m2 = addition_data

    assert m1 + m2 == Matrix([[11, 1], [8, 0]])


def test_equation_method(addition_data):
    m1, m2 = addition_data

    assert m1 != m2, f'Matrices: {m1} and {m2} are equal'

    assert m1 == Matrix([[2, 4], [5, -6]]), (f'Matrices: {m1} and '
                                             f'{Matrix([[2, 4], [5, -6]])}'
                                             f'  not equal')


if __name__ == '__main__':
    pytest.main()
