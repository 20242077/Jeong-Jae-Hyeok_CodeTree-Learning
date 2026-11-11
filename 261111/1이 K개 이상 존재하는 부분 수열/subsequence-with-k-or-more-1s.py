n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = { 1: 0, 2: 0 }

j = 0
ans = n+1
for i in range(n) :
    while j < n and dic[1] < k :
        dic[arr[j]] += 1
        j += 1
    if dic[1] >= k :
        ans = min(ans, j-i)
    dic[arr[i]] -= 1

print(ans if ans <= n else -1)