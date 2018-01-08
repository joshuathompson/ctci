def rotate_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    newMatrix = []

    for i in range(m):
        newMatrix.append([])
    
    for row in matrix:
        for coli, col in enumerate(row):
            newMatrix[coli].insert(0, col)

    return newMatrix

print(rotate_matrix(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
))