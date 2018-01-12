def recursiveMultiply(n, m, acc=0):
    if m <= 0:
        return acc
    return recursiveMultiply(n, m-1, acc+n)

print(recursiveMultiply(5, 6))