def sorted_merge(a, b):
    result = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        elif b[j] <= a[i]:
            result.append(b[j])
            j += 1

    result += a[i:]
    result += b[j:]

    print(result)


sorted_merge([1, 3], [2, 4])