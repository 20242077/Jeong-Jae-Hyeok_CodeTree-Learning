n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

vis = [[0]*n for _ in range(n)]

def dfs(x, y, idx) :
    area = 1
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)] :
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < n) :
            continue
        if grid[nx][ny] != idx or vis[nx][ny] == 1 :
            continue
        vis[nx][ny] = 1
        area += dfs(nx, ny, idx)
    
    return area


block_sizes = []

for i in range(n) :
    for j in range(n) :
        if vis[i][j] == 0 :
            vis[i][j] = 1
            block_sizes.append(dfs(i, j, grid[i][j]))

print(sum(1 for b in block_sizes if b >= 4), max(block_sizes))