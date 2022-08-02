def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30

        m3 = [
            [1,   2,  3,  4],
            [4,   5,  6,  7],
            [7,   8,  9, 10],
            [10, 11, 12, 13]
         ]
    """
    sum = 0

    for entry in matrix:
        sum += entry[matrix.index(entry)]
        sum += entry[-(matrix.index(entry) + 1)]

    return sum

# m2 = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
# ]
# print(sum_up_diagonals(m2))
# # 30