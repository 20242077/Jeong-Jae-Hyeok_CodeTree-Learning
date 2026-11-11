n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = j = 0
while i < n and j < m :
    if A[i] == B[j] :
        i += 1
        j += 1
    else :
        i += 1

if j == m :
    print("Yes")
else :
    print("No")