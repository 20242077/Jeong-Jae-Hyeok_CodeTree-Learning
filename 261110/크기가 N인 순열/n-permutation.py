n = int(input())

def backtrack(perm, idx) :
    if idx == n :
        print(*perm)
        return
    
    for i in range(1, n+1) :
        if i not in perm :
            perm.append(i)
            backtrack(perm, idx+1)
            perm.pop()

backtrack([], 0)