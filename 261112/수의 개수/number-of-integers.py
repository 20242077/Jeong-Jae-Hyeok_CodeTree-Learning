import bisect

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

for q in queries :
    ub = bisect.bisect_right(arr, q)
    lb = bisect.bisect_left(arr, q)
    print(ub-lb)