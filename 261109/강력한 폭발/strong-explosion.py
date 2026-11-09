n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [
    [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
    [(-1, 0), (0, 0), (1, 0), (0, -1), (0, 1)],
    [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]
]
bomb_pos = [] # 폭탄이 설치된 위치를 미리 저장

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 1 :
            bomb_pos.append((i, j))

ans = 0
k = len(bomb_pos)

def bomb(pos, x, y, i) :
    new_pos = pos.copy() # 이전 재귀 단계의 pos는 변경되지 않음

    for dx, dy in dirs[i] :
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n :
            new_pos.add((nx, ny))
    
    return new_pos


def backtrack(idx, pos) : # idx: 현재 종류를 결정할 폭탄의 인덱스
    global ans
    
    # 모든 폭탄 종류를 결정한 경우
    if idx == k :
        ans = max(ans, len(pos))
        return
    
    # 현재 폭탄 위치
    x, y = bomb_pos[idx]

    # 세 가지 폭탄 종류 모두 시도
    for typ in range(3) :
        new_pos = bomb(pos, x, y, typ)
        backtrack(idx+1, new_pos)

backtrack(0, set())
print(ans)