N, M = map(int, input().split())

def combination(comb, idx) :
    if idx == M :
        print(*comb)
        return
    
    for i in range(1, N+1) :
        if len(comb) > 0 and comb[-1] >= i :
            continue
        comb.append(i)
        combination(comb, idx+1)
        comb.pop()


combination([], 0)

        