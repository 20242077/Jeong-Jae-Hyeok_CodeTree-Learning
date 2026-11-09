n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

lines = sorted(list(zip(x1, x2)), key=lambda x: x[1])
prev_r = ans = 0

for l, r in lines :
    if prev_r < l :
        ans += 1
        prev_r = r

print(ans)