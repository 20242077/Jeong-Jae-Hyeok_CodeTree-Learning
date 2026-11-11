word, k = input().split()
k = int(k)

n = len(word)
i = j = 0
cnt = dict()
max_len = 1

while j < n :
    if word[j] in cnt  :
        cnt[word[j]] += 1
        j += 1
        max_len = max(max_len, j-i)
    elif len(cnt) < k :
        cnt[word[j]] = 1
        j += 1
    else :
        cnt[word[i]] -= 1
        if cnt[word[i]] == 0 :
            del cnt[word[i]]
        i += 1

print(max_len)