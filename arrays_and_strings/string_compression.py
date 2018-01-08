def string_compression(s):
    count = 0
    currentCharacter = None
    output = ''
    for c in s:
        if currentCharacter is None:
            currentCharacter = c
        elif currentCharacter != c:
            output += currentCharacter + str(count)
            currentCharacter = c
            count = 0
        count += 1

    output += currentCharacter + str(count)

    if len(output) > len(s):
        return s

    return output

print(string_compression("aabbccdd"))
print(string_compression("aabcccccaaa"))
print(string_compression("aabcccccaaabgfafqwr"))