board = [list(map(int, input().split())) for _ in range(19)]

def check(x, y) :
    if x < 0 or y < 0 or x >= 19 or y >= 19 :
        return 1
    return 0

color = 0
win = False
wx = wy = 0
for i in range(19) :
    for j in range(19) :
        if board[i][j] != 0 :
            color = board[i][j]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                            (-1, -1), (-1, 1), (1, -1), (1, 1)] :
                win = True
                for k in range(5) :
                    if check(i+dx*k, j+dy*k) :
                        win = False
                        break
                    if board[i+dx*k][j+dy*k] != color :
                        win = False
                        break
                else :
                    wx, wy = i+dx*2, j+dy*2
                    break
        if win :
            break
    if win :
        break

if wx == 0 and wy == 0 :
    print(0)
else :
    print(color)
    print(wx+1, wy+1)
    