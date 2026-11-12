M = int(input())
a, b = map(int, input().split())

max_turn, min_turn = 0, M

for target in range(a, b+1) :
    l, r, turn = 1, M, 0
    while l <= r :
        m = (l+r)//2
        turn += 1
        if m == target :
            min_turn = min(min_turn, turn)
            max_turn = max(max_turn, turn)
            break
        elif m < target :
            l = m+1
        else :
            r = m-1

print(min_turn, max_turn)