n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 각 정수를 크기 k로 잘랐을 때 나오는 조각의 총 개수가 m개 이상인지 확인하는 함수
def is_possible(k) :
    cnt = 0
    for num in arr :
        cnt += num//k
    return cnt >= m

# 이분탐색 범위 설정
l, r = 1, max(arr)
ans = 0

while l <= r :
    mid = (l+r)//2
    
    if is_possible(mid) :
        ans = mid # 가능한 경우 크기를 더 키워봄
        l = mid+1
    else :
        r = mid-1

print(ans)