import math

def one_away(a, b):
    if a == b:
        return True
    elif len(a) == len(b):
        changes_required = 0
        for i, c in enumerate(a):
            if c != b[i]:
                changes_required += 1

        return changes_required < 2
    elif math.fabs(len(a) - len(b)) <= 1:
        if len(a) > len(b):
            for i, c in enumerate(a):
                ns = a[:i] + a[i+1:]
                if ns == b:
                    return True
            return False
        else:
            for i, c in enumerate(b):
                ns = b[:i] + b[i+1:]
                if ns == a:
                    return True
            return False
    else:
        return False

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))