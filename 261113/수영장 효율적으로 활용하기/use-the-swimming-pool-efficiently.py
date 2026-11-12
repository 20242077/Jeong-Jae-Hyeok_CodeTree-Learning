import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(t) :
    time, lane = t, 1
    for num in arr :
        if time - num < 0 :
            lane += 1
            time = t
        time -= num
    
    if lane > m :
        return False
    return True

if n <= m :
    print(max(arr))
    sys.exit()

l, r = max(arr), sum(arr)
min_T = r

while l <= r :
    mid = (l+r)//2
    if is_possible(mid) :
        min_T = min(min_T, mid)
        r = mid - 1
    else :
        l = mid + 1

print(min_T)