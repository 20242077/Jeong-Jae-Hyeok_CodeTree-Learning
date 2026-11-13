N = int(input())
B = [int(input()) for _ in range(N)]

B_set = set(B)
A = [a for a in range(1, 2*N+1) if a not in B_set]
B.sort()

a_score, b = 0, 0

for a in range(N) :
    if B[b] < A[a] :
        a_score += 1
        b += 1

print(a_score)