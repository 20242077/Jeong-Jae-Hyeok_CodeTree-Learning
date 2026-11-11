n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = dict()
i = j = 0
max_len = 1

while j < n :
    if arr[j] in dic :
        if dic[arr[j]] < k :
            dic[arr[j]] += 1
            j += 1
            max_len = max(max_len, j - i)
        else :
            dic[arr[i]] -= 1
            if dic[arr[i]] == 0 :
                del dic[arr[i]]
            i += 1
    else :
        dic[arr[j]] = 1
        j += 1
        max_len = max(max_len, j - i)

print(max_len)