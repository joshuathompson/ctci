def triple_step(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)


print(triple_step(3))
print(triple_step(6))
print(triple_step(20))