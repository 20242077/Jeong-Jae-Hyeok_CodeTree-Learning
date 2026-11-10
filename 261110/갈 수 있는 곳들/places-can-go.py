from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]
vis = [[0]*n for _ in range(n)]
cnt = 0

for sx, sy in points :
    if vis[sx-1][sy-1] == 1 :
        continue
    vis[sx-1][sy-1] = 1
    cnt += 1
    q = deque([(sx-1, sy-1)])
    while q :
        x, y = q.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)] :
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n) :
                continue
            if grid[nx][ny] == 1 or vis[nx][ny] == 1 :
                continue
            vis[nx][ny] = 1
            cnt += 1
            q.append((nx, ny))

print(cnt)