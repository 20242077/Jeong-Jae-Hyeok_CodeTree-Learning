A = input()
n = len(A)

ans = 0
for i in range(n-2) :
    for j in range(i+2, n-1) :
        if A[i:i+2] == '((' and A[j:j+2] == '))' :
            ans += 1

print(ans)