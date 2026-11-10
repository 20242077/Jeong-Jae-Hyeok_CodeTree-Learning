n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

vis = [[0]*n for _ in range(n)]
population = []


def dfs(x, y) :
    local = 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n :
            continue
        if grid[nx][ny] == 0 or vis[nx][ny] == 1 :
            continue
        vis[nx][ny] = 1
        local += dfs(nx, ny)
    
    return local


for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 1 and vis[i][j] == 0 :
            vis[i][j] = 1
            local = dfs(i, j)
            population.append(local)

print(len(population))
population.sort()
for p in population :
    print(p)