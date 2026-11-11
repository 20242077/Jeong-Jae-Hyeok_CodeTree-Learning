word = input()
n = len(word)
i, j = 0, 0
s = set()

max_len = 0
while j < n :
    if word[j] not in s :
        s.add(word[j])
        max_len = max(max_len, len(s))
        j += 1
    else :
        s.remove(word[i])
        i += 1

print(max_len)