from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# 0: 이동가능, 1: 벽
vis = [[[0]*(k+1) for _ in range(n)] for _ in range(n)]
vis[r1][c1][0] = 0
q = deque([(r1, c1, 0, 0)])

while q :
    x, y, s, broke = q.popleft()
    if x == r2 and y == c2 :
        print(s)
        break
    
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)] :
        nx, ny = x+dx, y+dy
        if not (0 <= nx < n and 0 <= ny < n) :
            continue
        if grid[nx][ny] == 0 and vis[nx][ny][broke] == 0 :
            vis[nx][ny][broke] = 1
            q.append((nx, ny, s+1, broke))
        elif grid[nx][ny] == 1 and broke < k and vis[nx][ny][broke+1] == 0 :
            vis[nx][ny][broke+1] = 1
            q.append((nx, ny, s+1, broke+1))
else :
    print(-1)