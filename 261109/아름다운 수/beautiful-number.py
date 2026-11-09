n = int(input())

def func(n) :
    if n == 0 :
        return 1
    elif n < 0 :
        return 0
    local_ans = 0
    for i in range(1, 5) :
        local_ans += func(n - i)
    return local_ans

print(func(n))