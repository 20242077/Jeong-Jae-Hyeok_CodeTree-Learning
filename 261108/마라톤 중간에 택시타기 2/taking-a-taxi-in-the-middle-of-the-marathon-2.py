n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

cx, cy = x[0], y[0]
minDist = float('inf')
for i in range(1, n-1) : # 건너뛸 체크포인트
    dist = 0
    prev = 0
    for j in range(1, n) :
        if i == j :
            continue
        dist += abs(x[j]-x[prev]) + abs(y[j]-y[prev])
        prev = j # 인덱스 건너뛰기
    minDist = min(dist, minDist)

print(minDist)