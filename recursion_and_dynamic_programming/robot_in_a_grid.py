def robot_path(matrix, locationX, locationY, acc=[]):
    if locationX > len(matrix)-1 or locationY > len(matrix)-1:
        return
    elif locationX == len(matrix)-1 and locationY == len(matrix)-1:
        newList = acc.copy()
        newList.append("{},{}".format(locationX, locationY))
        print(newList)
        return
    elif matrix[locationY][locationX] == 0:
        newList = acc.copy()
        newList.append("{},{}".format(locationX, locationY))
        robot_path(matrix, locationX, locationY+1, newList)
        robot_path(matrix, locationX+1, locationY, newList)
    else:
        return

robot_path([
    [0, 1, 1],
    [0, 0, 0],
    [0, 0, 0]
], 0, 0)