def perm(prefix, word, acc):
    if len(word) == 0:
        if prefix not in acc:
            acc.append(prefix)
        return
    else:
        for index, s in enumerate(word):
            perm(prefix+s, word[:index] + word[index+1:], acc)

acc = []
perm("", "hello", acc)
print(acc)