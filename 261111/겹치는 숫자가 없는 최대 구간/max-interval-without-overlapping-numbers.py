n = int(input())
arr = list(map(int, input().split()))

i = 0
j = 1
s = {arr[0]}
max_len = 0

while j < n :
    if arr[j] not in s :
        s.add(arr[j])
        j += 1
        max_len = max(max_len, len(s))
    else :
        s.remove(arr[i])
        i += 1

print(max_len)