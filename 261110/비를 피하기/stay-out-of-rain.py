from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# 0: 이동 가능 칸
# 1: 벽 (이동불가)
# 2: 사람
# 3: 비를 피할 수 있는 칸

ans = [[0]*n for _ in range(n)]

# 사람 서 있는 좌표 저장
hpos = []
for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 2 :
            hpos.append((i, j))


for sx, sy in hpos :
    vis = [[0]*n for _ in range(n)]
    vis[sx][sy] = 1
    q = deque([(sx, sy, 0)])

    while q :
        x, y, s = q.popleft()
        if grid[x][y] == 3 :
            ans[sx][sy] = s
            break
        
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)] :
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n) :
                continue
            if grid[nx][ny] == 1 or vis[nx][ny] == 1:
                continue
            vis[nx][ny] = 1
            q.append((nx, ny, s+1))
    else :
        ans[sx][sy] = -1

for row in ans :
    print(*row)