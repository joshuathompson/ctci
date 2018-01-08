def palindrome_permutation(s):
    cMap = {}
    for c in s:
        if c == " ":
            continue

        if cMap.get(c, None) is None:
            cMap[c] = 1
        else:
            cMap[c] += 1

    odd_found = False

    for item in cMap:
        if cMap.get(item) % 2 != 0:
            if odd_found:
                return False 
            odd_found = True
    
    return True

print(palindrome_permutation("racecar"))
print(palindrome_permutation("racecars"))
print(palindrome_permutation("a nut for a jar of tuna"))
print(palindrome_permutation("wrong"))