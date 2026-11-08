n = int(input())
numbers = list(map(int, input().split()))

maxval = 0
for i in range(n-2) :
    for j in range(i+2, n) :
        maxval = max(maxval, numbers[i] + numbers[j])

print(maxval)