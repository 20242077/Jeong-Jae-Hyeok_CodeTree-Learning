n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for x, y in edges :
    graph[x].append(y)
    graph[y].append(x)

vis = [0]*(n+1)
ans = 0

def dfs(cur) :
    global ans
    vis[cur] = 1
    
    for nxt in graph[cur] :
        if vis[nxt] == 0 :
            ans += 1
            dfs(nxt)

dfs(1)
print(ans)