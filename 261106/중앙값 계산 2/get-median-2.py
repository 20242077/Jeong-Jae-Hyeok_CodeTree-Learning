n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
finArr = []
i = 1
while i <= len(arr) :
    if i == 1 :
        finArr.append(arr[0])
    else :
        arr2 = arr[:i]
        arr2.sort()
        idx = i//2
        v = arr2[idx]
        finArr.append(v)
    i += 2

for word in finArr :
    print(word, end = " ")