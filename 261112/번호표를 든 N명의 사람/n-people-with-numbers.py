import heapq

N, T_max = map(int, input().split())
d = [int(input()) for _ in range(N)]

def calc(k) :
    q = d[:k]
    for i in range(k, N) :
        t = heapq.heappop(q)
        heapq.heappush(q, t+d[i])
    
    return max(q)

l, r = 1, N
min_k = float('inf')

while l <= r :
    m = (l+r)//2
    t = calc(m)
    
    if t <= T_max :
        min_k = m
        r = m-1
    else :
        l = m+1

print(min_k)