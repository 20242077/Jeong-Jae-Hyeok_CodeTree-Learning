K, N = map(int, input().split())

def backtrack(idx, res) :
    if idx == N :
        print(*res)
        return

    for i in range(1, K+1) :
        if len(res) >= 2 and res[-2] == i and res[-1] == i :
            continue
        res.append(i)
        backtrack(idx+1, res)
        res.pop()

backtrack(0, [])