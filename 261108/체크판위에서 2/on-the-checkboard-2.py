R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

ans = 0
color = grid[0][0]
sx = sy = 0
if grid[R-1][C-1] != color :
    for i in range(sx+1, R-2) :
        for j in range(sy+1, C-2) :
            if grid[i][j] != color :
                for m in range(i+1, R-1) :
                    for n in range(j+1, C-1) :
                        if grid[m][n] == color :
                            ans += 1

print(ans)