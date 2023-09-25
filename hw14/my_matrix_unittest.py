"""Module for testing Matrices with unittest."""

import unittest

from hw11.my_matrix import Matrix


class TestCaseMatrix(unittest.TestCase):
    """class TestCaseMatrix."""

    def setUp(self) -> None:
        print('Test begin')
        self.m1 = Matrix([[3, 6, 7], [5, -3, 0]])
        self.m2 = Matrix([[1, 1], [2, 1], [3, -3]])
        self.m3 = Matrix([[2, 4], [5, -6]])
        self.m4 = Matrix([[9, -3], [3, 6]])

        self.mul_result = Matrix([[36, -12], [-1, 2]])
        self.add_result = Matrix([[11, 1], [8, 0]])

    def tearDown(self) -> None:
        print('Test end')

    def test_multiply_method(self):
        self.assertEqual(self.m1 * self.m2, self.mul_result)

    def test_addition_method(self):
        self.assertEqual(self.m3 + self.m4, self.add_result)

    def test_equation_method(self):
        self.assertNotEqual(self.m3, self.m2)
        self.assertEqual(self.m3, Matrix([[2, 4], [5, -6]]))


if __name__ == '__main__':
    unittest.main()
