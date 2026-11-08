n = int(input())
a = [int(input()) for _ in range(n)]

minDist = float('inf')
for i in range(n) : # i : 출발하는 방 번호
    dist = 0
    for j in range(n) :
        if i < j : 
            dist += (j-i)*a[j]
        elif i > j :
            dist += (n-(i-j))*a[j]
    minDist = min(minDist, dist)

print(minDist)