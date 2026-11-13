import heapq

n = int(input())
q = list(map(int, input().split()))
heapq.heapify(q)
ans = 0

while len(q) >= 2 :
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a+b)
    ans += a+b

print(ans)