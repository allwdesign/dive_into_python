def matrix_transposition(matrix: list) -> list:
    """Function to transpose a matrix.

    :param matrix: list
    :return: list
    """
    # Not use this: [[None]*len(matrix)] * len(matrix[0]),
    # in that case every cell of the list refers to the same address in
    # memory
    # result: [[None, None], [None, None], [None, None]]
    result = [[None for _ in range(len(matrix))] for _ in
              range(len(matrix[0]))]

    for idx_row in range(len(matrix)):  # idx_row: 0 1
        for idx_col in range(len(matrix[idx_row])):  # idx_col: 0 1 2
            result[idx_col][idx_row] = matrix[idx_row][idx_col]
    return result


if __name__ == '__main__':
    matrix_1 = [[1, 2, 3], [4, 5, 6]]
    matrix_2 = [[3, 3, 5, -2], [1, 1, 3, -2], [2, 2, 8, -3], [2, 2, 4, -1]]
    # After: [[1, 4], [2, 5], [3, 6]]
    print(f'Before: {matrix_1} After: {matrix_transposition(matrix_1)}')
    # After [[3, 1, 2, 2], [3, 1, 2, 2], [5, 3, 8, 4], [-2, -2, -3, -1]]
    print(f'Before: {matrix_2} After: {matrix_transposition(matrix_2)}')
