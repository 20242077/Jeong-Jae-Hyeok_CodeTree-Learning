n = int(input())
a = list(map(int, input().split()))
a.sort()

i, j, ans = 0, n-1, float('inf')

while i < j :
    m = a[i] + a[j]

    if abs(m) < ans :
        ans = abs(m)
    if m < 0 :
        i += 1
    elif m > 0 :
        j -= 1
    else :
        break

print(ans)