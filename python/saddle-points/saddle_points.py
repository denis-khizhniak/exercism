import numpy as np


def saddle_points(matrix):
    validate_matrix(matrix)

    arr = np.array(matrix)

    return [
        {"row": i + 1, "column": j + 1}
        for i in range(len(arr))
        for j in range(len(arr[i]))
        if arr[i, j] >= max(arr[i, :]) and arr[i, j] <= min(arr[:, j])
    ]


def validate_matrix(matrix):
    rows_lengths = [len(row) for row in matrix]
    if len(rows_lengths) > 0 and min(rows_lengths) != max(rows_lengths):
        raise ValueError("This matrix is irregular!")
