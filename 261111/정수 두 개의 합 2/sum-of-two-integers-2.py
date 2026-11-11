n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

i, j = 0, n-1
ans = 0

while i < j :
    s = arr[i] + arr[j]
    if s <= k :
        ans += j - i
        i += 1
    else :
        j -=1

print(ans)