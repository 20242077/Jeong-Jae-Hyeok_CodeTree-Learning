from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dirs = [(-1, -2), (-1, 2), (1, -2), (1, 2),
        (2, 1), (2, -1), (-2, -1), (-2, 1)]

vis = [[0]*n for _ in range(n)]
vis[r1-1][c1-1] = 1
q = deque([(r1-1, c1-1, 0)])

while q :
    x, y, step = q.popleft()
    if x == r2-1 and y == c2-1 :
        print(step)
        break
    for dx, dy in dirs :
        nx, ny = x+dx, y+dy
        if not (0 <= nx < n and 0 <= ny < n) :
           continue
        if vis[nx][ny] == 0 :
            vis[nx][ny] = 1
            q.append((nx, ny, step+1))
else :
    print(-1)
