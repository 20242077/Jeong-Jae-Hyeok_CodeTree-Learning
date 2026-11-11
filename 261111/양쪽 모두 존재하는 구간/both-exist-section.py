from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))

inner = [0]*(m+1)
outer = [0]*(m+1)

out_distinct = 0
for x in arr :
    if outer[x] == 0 :
        out_distinct += 1
    outer[x] += 1

in_distinct = 0

def push(x) :
    global in_distinct, out_distinct
    
    if inner[x] == 0 :
        in_distinct += 1
    inner[x] += 1
    
    outer[x] -= 1
    if outer[x] == 0 :
        out_distinct -= 1

def pop(x) :
    global in_distinct, out_distinct
    
    if outer[x] == 0 :
        out_distinct += 1
    outer[x] += 1
    
    inner[x] -= 1
    if inner[x] == 0 :
        in_distinct -= 1


j = 0
ans = n + 1

for i in range(n) :
    while j < n and in_distinct < m :
        push(arr[j])
        j += 1

    if in_distinct == m and out_distinct == m :
        ans = min(ans, j - i)
   
    pop(arr[i])

print(ans if ans <= n else -1)