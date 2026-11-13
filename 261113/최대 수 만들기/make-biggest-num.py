from functools import cmp_to_key

n = int(input())
arr = [int(input()) for _ in range(n)]

def compare(x, y) :
    if x + y > y + x : # x가 y보다 먼저 옴
        return -1
    elif x + y < y + x : # y가 x보다 먼저 옴
        return 1
    else :
        return 0

arr = list(map(str, arr))
arr.sort(key=cmp_to_key(compare))

for e in arr :
    print(e, end="")