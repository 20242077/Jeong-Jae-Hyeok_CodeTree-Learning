n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

cx, cy = x[0], y[0]
minDist = float('inf')
for i in range(1, n-1) : # 건너뛸 체크포인트
    dist = 0
    for j in range(n-1) :
        if i == j :
            continue
        elif i == j+1 :
            dist += abs(x[j+2] - x[j]) + abs(y[j+2] - y[j])
        else :
            dist += abs(x[j+1] - x[j]) + abs(y[j+1] - y[j])
    minDist = min(dist, minDist)

print(minDist)