"""Module for testing Matrices with pytest."""

import pytest

from hw11.my_matrix import Matrix


def test_multiply():
    m1 = Matrix([[3, 6, 7], [5, -3, 0]])
    m2 = Matrix([[1, 1], [2, 1], [3, -3]])
    mul_result = Matrix([[36, -12], [-1, 2]])

    assert m1 * m2 == mul_result


def test_addition_method():
    m1 = Matrix([[2, 4], [5, -6]])
    m2 = Matrix([[9, -3], [3, 6]])
    add_result = Matrix([[11, 1], [8, 0]])

    assert m1 + m2 == add_result


def test_equation_method():
    m1 = Matrix([[2, 4], [5, -6]])
    m2 = Matrix([[9, -3], [3, 6]])
    assert m1 != m2, f'Matrices: {m1} and {m2} are equal'

    assert m1 == Matrix([[2, 4], [5, -6]]), (f'Matrices: {m1} and '
                                             f'{Matrix([[2, 4], [5, -6]])}'
                                             f'  not equal')


if __name__ == '__main__':
    pytest.main()
