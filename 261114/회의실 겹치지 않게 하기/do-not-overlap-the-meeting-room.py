import heapq

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

q = []
drop = 0

for s, e in meetings :
    if q and q[0][1] <= s :
        heapq.heappop(q)
        heapq.heappush(q, (s, e))
    elif q and q[0][1] > s :
        drop += 1
    else :
        heapq.heappush(q, (s, e))

print(drop)