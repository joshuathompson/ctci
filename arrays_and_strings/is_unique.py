def is_unique(s):
    m = {}
    for c in s:
        if m.get(c, None) is not None:
            return False
        else:
            m[c] = 1
    
    return True

def is_unique_no_ds(s):
    sortedS = sorted(s)
    last = ''
    for c in sortedS:
        if last != '' and last == c:
            return False
        else:
            last = c

    return True

print(is_unique("abbc"))
print(is_unique("abc"))
print(is_unique("abcfagbza"))
print(is_unique_no_ds("abbc"))
print(is_unique_no_ds("abc"))
print(is_unique_no_ds("abcfagbza"))