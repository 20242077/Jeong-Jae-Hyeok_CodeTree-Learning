n, s = map(int, input().split())
arr = list(map(int, input().split()))

i = j = 0
partial_sum = arr[0]
ans = n+1

while j < n :
    if partial_sum < s :
        j += 1
        if j < n :
            partial_sum += arr[j]
    else :
        ans = min(ans, j-i+1)
        if i < j :
            partial_sum -= arr[i]
            i += 1
    if ans == 1 :
        break

if ans == n+1 :
    print(-1)
else:
    print(ans)
