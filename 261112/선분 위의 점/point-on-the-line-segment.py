from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

points.sort()

for s, e in segments :
    # s 이상인 첫 위치
    left_index = bisect_left(points, s)

    # e 이하인 마지막 위치
    right_index = bisect_right(points, e)
    
    print(right_index - left_index)
