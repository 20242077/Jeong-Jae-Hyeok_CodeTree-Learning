n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))
time = []

fires.sort()
stations.sort()

j = 0
for i in range(n) :
    nxt = float('inf')
    while j+1 < m and stations[j+1] < fires[i] :
        j += 1
    prev = fires[i] - stations[j]
    if j+1 < m :
        nxt = stations[j+1] - fires[i]
    
    time.append(min(prev, nxt))

print(max(time))