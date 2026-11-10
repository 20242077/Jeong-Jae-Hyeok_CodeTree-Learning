from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

vis = [[-1]*m for _ in range(n)]
vis[0][0] = 0
q = deque([(0, 0)])
while q :
    x, y = q.popleft()
    if x == n-1 and y == m-1 :
        print(vis[n-1][m-1])
        break
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)] :
        nx, ny = x+dx, y+dy
        if not (0 <= nx < n and 0 <= ny < m) :
            continue
        if a[nx][ny] == 0 or vis[nx][ny] >= 0 :
            continue
        vis[nx][ny] = vis[x][y] + 1
        q.append((nx, ny))
else :
    print(-1)