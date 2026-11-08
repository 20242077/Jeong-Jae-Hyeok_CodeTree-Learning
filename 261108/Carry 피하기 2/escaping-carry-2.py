n = int(input())
arr = [int(input()) for _ in range(n)]

ans = -1
for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            digit = len(str(max(arr[i], arr[j], arr[k])))
            x, y, z = arr[i], arr[j], arr[k]
            for d in range(digit) :
                if x%10 + y%10 + z%10 >= 10 :
                    break
                x /= 10
                y /= 10
                z /= 10
            else :
                ans = max(arr[i] + arr[j] + arr[k], ans)

print(ans)