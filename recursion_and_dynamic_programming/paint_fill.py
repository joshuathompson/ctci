def paint_fill(matrix, x, y):
    if x >= 0 and x < len(matrix[0]) and y >= 0 and y < len(matrix):
        if matrix[y][x] != 0:
            return
        else:
            matrix[y][x] = 1
            print("Painting {}, {}".format(x, y))
            paint_fill(matrix, x+1, y)
            paint_fill(matrix, x-1, y)
            paint_fill(matrix, x, y+1)
            paint_fill(matrix, x, y-1)
    else:
        return

matrix = [
    [0, 2, 2, 2, 0],
    [0, 0, 0, 0, 0],
    [2, 2, 0, 2, 0],
    [2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0]
]

paint_fill(matrix, 1, 1)

print(matrix)