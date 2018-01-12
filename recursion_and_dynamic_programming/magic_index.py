def magic_index(arr, start, end):
    if end < start:
        return 0

    index = int(start+end / 2)

    if arr[index] == index:
        return arr[index]
    elif index < arr[index]:
        return magic_index(arr, start, index-1)
    elif index > arr[index]:
        return magic_index(arr, index+1, end)

arr = [-1, 0, 1, 2, 5, 6, 7, 8, 9, 10]
magic_number = magic_index(arr, 0, len(arr)-1)
print(magic_number)