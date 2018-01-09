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
    n = len(matrix[0])
    count = 0

    while n != 1:
        
        for i in range(n-1):
            tl = matrix[count][count+i]
            tr = matrix[count+i][count+n-1]
            br = matrix[count+n-1][count+n-i-1]
            bl = matrix[count+n-i-1][count]

            matrix[count][i+count] = bl
            matrix[count+i][count+n-1] = tl
            matrix[count+n-1][count+n-i-1] = tr
            matrix[count+n-i-1][count] = br

        n = n/2
        count += 1

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