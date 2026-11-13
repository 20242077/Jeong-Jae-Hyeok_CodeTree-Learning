from bisect import bisect_left, bisect_right

n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]

x.sort()

# 반경 R일 때 K개 이하의 폭탄으로 모든 점을 제거할 수 있는지 확인하는 함수
def can_remove_all(r) :
    bombs_used = 1
    # 첫 번째 폭탄은 가장 왼쪽 점(x[0])을 포함하면서 최대한 오른쪽까지 덮도록
    # 즉, 폭탄 투하 위치는 x[0] + r 이며, 커버 범위는 x[0] + 2*r 까지임
    limit = x[0] + 2*r
    
    for i in range(1, n) :
        if x[i] > limit :
            bombs_used += 1
            limit = x[i] + 2*r
            if bombs_used > k :
                return False
    return True


l, r = 0, x[-1]-x[0]
min_r = r

while l <= r :
    m = (l+r)//2

    if can_remove_all(m) :
        min_r = min(m, min_r)
        r = m-1
    else :
        l = m+1

print(min_r)