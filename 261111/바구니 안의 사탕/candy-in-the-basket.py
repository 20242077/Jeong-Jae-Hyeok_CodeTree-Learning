n, k = map(int, input().split()) # n : 바구니 개수, c : 중심점, k : c-k ~ c+k 구간
candy_pos = [tuple(map(int, input().split())) for _ in range(n)]
candy_pos.sort(key=lambda x: (x[1], x[0]))
dic = {}
for c, p in candy_pos :
    if p not in dic :
        dic[p] = 0
    dic[p] += c    

s = candy_pos[0][1] - 1
e = (s+1) + 2*k
candy_sum = 0
for pos, candy in dic.items() :
    if s+1 <= pos <= e :
        candy_sum += candy

max_candy = candy_sum

while e < candy_pos[-1][1] :
    s += 1
    e += 1
    if s in dic :
        candy_sum -= dic[s]
    if e in dic :
        candy_sum += dic[e]
    max_candy = max(candy_sum, max_candy)

print(max_candy)