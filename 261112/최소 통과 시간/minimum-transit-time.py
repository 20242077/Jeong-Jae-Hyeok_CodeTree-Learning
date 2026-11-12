n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

l, r = min(arr), max(arr)*n

def calc(t) :
    cnt = 0
    for dur in arr :
        cnt += t//dur
    return cnt

min_t = float('inf')

while l <= r :
    mid = (l+r)//2
    cnt = calc(mid)
    
    if cnt >= n :
        min_t = min(min_t, mid)
        r = mid-1
    else :
        l = mid+1

print(min_t)