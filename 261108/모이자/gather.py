n = int(input())
A = list(map(int, input().split()))

minDist = float('inf')
for i in range(n) :
    dist = 0
    for j in range(n) :
        if i == j :
            continue
        dist += A[j]*abs(i-j)
    if dist < minDist :
        minDist = dist

print(minDist)