def string_rotation(a, b):
    length = len(a)

    for i in range(length):
        na = a[len(a)-1:] + a[:len(a)-1]
        if a == b:
            return True
        a = na

    return False

print(string_rotation("erbottlewat", "waterbottle"))