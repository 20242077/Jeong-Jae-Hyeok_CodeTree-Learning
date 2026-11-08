n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

maxCoin = 0 
for i in range(n) :
    for j in range(n - 2) :
        maxCoin = max(maxCoin, sum(grid[i][j:j+3]))

print(maxCoin)