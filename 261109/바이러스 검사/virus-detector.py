import math

n = int(input())
customers = list(map(int, input().split()))
leader, member = map(int, input().split())
ans = 0

for c in customers :
    rem = c - leader
    ans += 1
    if rem <= 0 :
        continue
    ans += math.ceil(rem/member)
print(ans)