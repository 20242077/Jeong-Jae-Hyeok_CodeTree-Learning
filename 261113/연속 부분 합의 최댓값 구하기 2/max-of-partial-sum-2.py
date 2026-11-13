n = int(input())
a = list(map(int, input().split()))

ans, s = a[0], 0

for i in a :
    s = max(s+i, i)
    ans = max(ans, s)

print(ans)