n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 0: 비어있음, 1: 귤, 2: 상한 귤
rotten = []
vis = [[-1]*n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 2 :
            vis[i][j] = 0
            rotten.append((i, j))
        elif grid[i][j] == 1 :
            vis[i][j] = -2

new_rotten = []

def spread(x, y) :
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)] :
        nx, ny = x+dx, y+dy
        if not (0 <= nx < n and 0 <= ny < n) :
            continue
        if grid[nx][ny] == 0 or vis[nx][ny] >= 0 :
            continue
        vis[nx][ny] = vis[x][y] + 1
        new_rotten.append((nx, ny))
    

while len(rotten) :
    new_rotten = []
    for sx, sy in rotten :
        spread(sx, sy)
    rotten = new_rotten

for row in vis :
    print(*row)
        