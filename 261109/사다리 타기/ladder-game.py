from collections import defaultdict

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

edges.sort(key=lambda x: x[1])
ladders = [(x[0], x[0]+1) for x in edges]
res = defaultdict(int) # 사다리타기 결과
ans = m


# 사다리타기 결과 계산
def run_ladder(ladders, start) :
    cur = start
    
    for lad in ladders :
        left, right = lad[0], lad[1]
        
        if cur == left :
            cur = right
        elif cur == right :
            cur = left
    
    return cur


# 백트래킹 조합 탐색
def backtrack(lines, idx) :
    global ans

    if idx == m :
        for i in range(1, n+1) :
            if run_ladder(lines, i) != res[i] :
                break
        else :
            ans = min(ans, len(lines))
        return
    
    lines.append(ladders[idx])
    backtrack(lines, idx+1) # idx번째 가로선을 선택할 경우
    lines.pop()

    backtrack(lines, idx+1) # idx번째 가로선을 선택하지 않을 경우


# 메인 코드
for i in range(1, n+1) :
    res[i] = run_ladder(ladders, i)


backtrack([], 0)
print(ans)