import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

vis = [[0]*m for _ in range(n)]
max_height = max(map(max, grid))


def dfs(x, y, k) :
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)] :
        nx, ny = x+dx, y+dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m :
            continue
        if grid[nx][ny] <= k or vis[nx][ny] == 1 :
            continue
        vis[nx][ny] = 1
        dfs(nx, ny, k)

max_area = 0
ans_k = 1

for k in range(1, max_height+1) :
    area = 0
    vis = [[0]*m for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            if grid[i][j] > k and vis[i][j] == 0 :
                vis[i][j] = 1
                area += 1
                dfs(i, j, k)
    
    if area > max_area :
        max_area = area
        ans_k = k

print(ans_k, max_area)