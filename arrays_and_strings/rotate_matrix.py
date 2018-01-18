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

def rotate_square_matrix(matrix):
    size = len(matrix)
    layers = size/2

    for l in range(layers):
        for i in range(l, size-1-l):
            tl = matrix[l][i]
            tr = matrix[i][size-1-l]
            br = matrix[size-1-l][size-1-i]
            bl = matrix[size-1-i][l]

            matrix[l][i] = bl
            matrix[i][size-1-l] = tl
            matrix[size-1-l][size-1-i] = tr
            matrix[size-1-i][l] = br

    return matrix

print(rotate_matrix(
    [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
))

print(rotate_square_matrix(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
))