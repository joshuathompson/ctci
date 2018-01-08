def zero_matrix(matrix):
    zero_columns = []
    zero_rows = []
    for rowi, row in enumerate(matrix):
        for coli, col in enumerate(row):
            if col == 0:
                zero_rows.append(rowi)
                zero_columns.append(coli)

    for rowi, row in enumerate(matrix):
        for coli, col in enumerate(row):
            if rowi in zero_rows:
                matrix[rowi][coli] = 0
            elif coli in zero_columns:
                matrix[rowi][coli] = 0 

    return matrix


print(zero_matrix([
    [1, 0, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0]
]))