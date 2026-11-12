target = int(input())

l, r, max_n = 1, target, 0
while l <= r :
    m = (l+r)//2
    s = m*(m+1)//2
    if s <= target :
        max_n = max(max_n, m)
        l = m+1
    else :
        r = m-1
print(max_n)
