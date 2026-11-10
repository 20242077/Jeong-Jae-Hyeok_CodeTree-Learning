from collections import deque

N = int(input())

# -1, +1, 2의 약수일 경우 /2, 3의 약수일 경우 /3
vis = [0]*(N+3)
vis[N] = 1
q = deque([(N, 0)])

while q :
    n, cnt = q.popleft()
    if n == 1 :
        print(cnt)
        break
    
    if n-1 >= 0 and vis[n-1] == 0 :
        vis[n-1] = 1
        q.append((n-1, cnt+1))
    if n+1 < N+3 and vis[n+1] == 0 :
        vis[n+1] = 1
        q.append((n+1, cnt+1))
    if n%2 == 0 and vis[n//2] == 0 :
        vis[n//2] = 1
        q.append((n//2, cnt+1))
    if n%3 == 0 and vis[n//3] == 0 :
        vis[n//3] = 1
        q.append((n//3, cnt+1))
