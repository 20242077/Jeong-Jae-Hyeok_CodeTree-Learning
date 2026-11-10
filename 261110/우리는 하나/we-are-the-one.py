# 9:52
from collections import deque
from itertools import combinations

n, k, u, d = map(int, input().split()) # n 격자 크기, k 도시 수, 높이 차 u ~ d
grid = [list(map(int, input().split())) for _ in range(n)]

vis = [[0]*n for _ in range(n)]
points = []

for i in range(n) :
    for j in range(n) :
        points.append((i, j))


def linkable(x, y) :
    link = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < n) :
            continue
        if vis[nx][ny] == 1 :
            continue
        if u <= abs(grid[nx][ny] - grid[x][y]) <= d :
            vis[nx][ny] = 1
            link += linkable(nx, ny)

    return link


ans = 0

for cities in combinations(points, k) :
    links = 0
    vis = [[0]*n for _ in range(n)]
    for x, y in cities :
        if vis[x][y] == 0 :
            vis[x][y] = 1
            links += linkable(x, y)
    ans = max(links, ans)

print(ans)