def check_permutation(a, b):
    aMap = {}
    for c in a:
        if aMap.get(c, None) is None:
            aMap[c] = 0
        else:
            aMap[c] += 1
    
    bMap = {}
    for c in b:
        if bMap.get(c, None) is None:
            bMap[c] = 0
        else:
            bMap[c] += 1

    for item in aMap:
        if aMap.get(item, None) != bMap.get(item, None):
            return False

    for item in bMap:
        if aMap.get(item, None) != bMap.get(item, None):
            return False

    return True

def check_permutation_simple(a, b):
    aSorted = sorted(a)
    bSorted = sorted(b)

    if aSorted == bSorted:
        return True

    return False

print(check_permutation("abc", "cab"))
print(check_permutation("abacdef", "fedcbaa"))
print(check_permutation("abb", "ab"))
print(check_permutation_simple("abcdef", "fedcba"))
print(check_permutation_simple("ab", "abb"))