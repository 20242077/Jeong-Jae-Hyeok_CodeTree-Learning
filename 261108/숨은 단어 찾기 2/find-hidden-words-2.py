N, M = map(int, input().split())
arr = [input() for _ in range(N)]

def check(x, y, N, M) :
    if x < 0 or y < 0 or x >= N or y >= M :
        return 1
    return 0

ans = 0
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 'L' :
            for dx, dy in [(-1, 0), (-1, 1), (1, 0), (1, -1), 
                            (1, 1), (-1, -1), (0, 1), (0, -1)] :
                if check(i+dx, j+dy, N, M) or check(i+2*dx, j+2*dy, N, M) :
                    continue
                if arr[i+dx][j+dy] == 'E' and arr[i+2*dx][j+2*dy] == 'E' :
                    ans += 1
print(ans)