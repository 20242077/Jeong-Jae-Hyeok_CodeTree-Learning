from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
mx = grid[r-1][c-1]

def find_next_pos(sx, sy) :
    global mx
    vis = [[0]*n for _ in range(n)]
    q = deque([(sx, sy)])
    mx_val, mx_x, mx_y = 0, -1, -1

    while q :
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)] :
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n) :
                continue
            if grid[nx][ny] >= mx or vis[nx][ny] == 1 :
                continue
            vis[nx][ny] = 1
            if grid[nx][ny] > mx_val :
                mx_val = grid[nx][ny]
                mx_x, mx_y = nx, ny
            elif grid[nx][ny] == mx_val :
                if nx < mx_x :
                    mx_x, mx_y = nx, ny
                elif nx == mx_x and ny < mx_y :
                    mx_y = ny
            q.append((nx, ny))
    
    return mx_x, mx_y, mx_val
 

x, y = r-1, c-1

for _ in range(k) :
    nx, ny, mx_val = find_next_pos(x, y)
    if nx == -1 and ny == -1 :
        break
    x, y = nx, ny
    mx = mx_val

print(x+1, y+1)