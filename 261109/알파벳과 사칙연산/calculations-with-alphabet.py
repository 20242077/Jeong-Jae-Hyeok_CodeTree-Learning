from collections import defaultdict

expression = input()

n = len(expression)//2 + 1
ans = -float('inf')
nums, ops = [], []  

for i, c in enumerate(expression) :
    if c.isalpha() :
        nums.append(c)
    else :
        ops.append(c)


def calc(dic) :
    res = dic[nums[0]]
    for i, op in enumerate(ops) :
        if op == '+' :
            res += dic[nums[i+1]]
        elif op == '-' :
            res -= dic[nums[i+1]]
        else :
            res *= dic[nums[i+1]]
    
    return res


def backtrack(idx, dic) :
    global ans
    
    if idx == n :
        ans = max(ans, calc(dic))
        return

    if dic[nums[idx]] == 0 :
        for val in range(1, 5) :
            dic[nums[idx]] = val
            backtrack(idx+1, dic)
            dic[nums[idx]] = 0
    else :
        backtrack(idx+1, dic)
        

backtrack(0, defaultdict(int))
print(ans)