n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))


for target in query :
    pos = n
    l, r = 0, n-1
    while l <= r :
        m = (l+r)//2
        if arr[m] >= target :
            if arr[m] == target :
                pos = min(pos, m)
            r = m-1
        else :
            l = m+1
    print(pos+1 if pos < n else -1)
