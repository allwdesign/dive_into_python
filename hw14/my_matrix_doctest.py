"""Module for testing Matrices with doctest."""

import numpy as np


class Matrix:
    """
        Class Matrix.
    # Multiplication of two Matrices
    >>> m1 = Matrix([[3, 6, 7], [5, -3, 0]])
    >>> m2 = Matrix([[1, 1], [2, 1], [3, -3]])
    >>> print(m1 * m2)
    [[ 36 -12]
     [ -1   2]]

    # Addition of two Matrices
    >>> m3 = Matrix([[2, 4], [5, -6]])
    >>> m4 = Matrix([[9, -3], [3, 6]])
    >>> print(m3 + m4)
    [[11  1]
     [ 8  0]]


    # Equal
    >>> print('m3 == m2:', m3 == m2)
    m3 == m2: False
    >>> print('m3 == m3:', m3 == m3)
    m3 == m3: True

    # Get item
    >>> print(m1[0])
    [3 6 7]
    """

    def __init__(self, matrix_data):
        """Constructor."""
        self.rows = len(matrix_data)
        self.columns = len(matrix_data[0])
        self.matrix = np.array(matrix_data)

    def __getitem__(self, idx):
        """Get matrix item."""
        return self.matrix[idx]

    def __eq__(self, other):
        """Method compares matrices."""
        return np.array_equal(self.matrix, other.matrix)

    def __lt__(self, other):
        """Method(less than) compares matrices by the number of rows."""
        return self.rows < other.rows

    def __gt__(self, other):
        """Method(greate than) compares matrices by the number of rows."""
        return self.rows > other.rows

    def __add__(self, other):
        """Addition of two Matrices"""
        return Matrix(self.matrix + other.matrix)

    def __mul__(self, other):
        """Multiplication of two Matrices"""
        return Matrix(self.matrix.dot(other.matrix))

    def __str__(self):
        """String representation."""
        return f'{self.matrix}'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
