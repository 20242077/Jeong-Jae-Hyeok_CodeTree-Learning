A = input()

n = len(A)
ans = 0

for i in range(n-1) :
    for j in range(i+1, n) :
        if A[i] == '(' and A[j] == ')' :
            ans += 1

print(ans)