import heapq

N = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(N)]
bombs.sort(key=lambda x: -x[1])

q = []
idx, ans = 0, 0
max_time = max(x[1] for x in bombs)

for t in range(max_time, 0, -1) :
    while idx < N and bombs[idx][1] >= t :
        heapq.heappush(q, -bombs[idx][0])
        idx += 1
    
    if q :
        ans += -heapq.heappop(q)

print(ans)