n = int(input())
price = list(map(int, input().split()))

stk = []
max_profit = 0

for i in range(n) :
    if stk and price[i] < price[stk[-1]] :
        stk.append(i)
    elif stk :
        max_profit = max(max_profit, price[i] - price[stk[-1]])
    else :
        stk.append(i)

print(max_profit)