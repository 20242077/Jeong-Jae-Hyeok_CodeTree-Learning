n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

vis = [[0]*m for _ in range(n)]
ans = 0

def dfs(x, y) :
    global ans
    
    if x == n-1 and y == m-1 :
        ans = 1
        return
    
    for dx, dy in [(1, 0), (0, 1)] :
        nx, ny = x + dx, y + dy
        if nx >= n or ny >= m :
            continue
        if grid[nx][ny] == 0 or vis[nx][ny] == 1 :
            continue
        vis[nx][ny] = 1
        dfs(nx, ny)

vis[0][0] = 1
dfs(0, 0)
print(ans)