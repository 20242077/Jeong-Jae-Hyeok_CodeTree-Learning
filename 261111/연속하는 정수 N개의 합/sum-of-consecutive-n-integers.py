n, m = map(int, input().split())
arr = list(map(int, input().split()))

i = -1
j = 0
s = arr[0]
ans = 0

while j < n :
    if s >= m :
        if s == m :
            ans += 1
        i += 1
        s -= arr[i]
    else :
        j += 1
        if j < n :
            s += arr[j]

print(ans)

