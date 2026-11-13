import heapq

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
q = []
heapq.heappush(q, (meetings[0][0], meetings[0][1]))
cnt = 1

for s, e in meetings :
    if q and q[0][1] <= s :
        cnt += 1
        heapq.heappop(q)
        heapq.heappush(q, (s, e))

print(cnt)