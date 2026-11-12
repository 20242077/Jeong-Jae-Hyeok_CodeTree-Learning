MAX = 10_000_000_000
target = int(input())

def count_35(n) :
    cnt = n//3 + n//5 - n//15
    return cnt

l, r = 1, MAX

while l <= r :
    m = (l+r)//2
    cnt = count_35(m)
    if m - cnt == target and m % 3 != 0 and m % 5 != 0 :
        print(m)
        break
    elif m - cnt < target :
        l = m+1
    else :
        r = m-1
