n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
def bubble_sort(arr) :
    n = len(arr)
    for i in range(n) :
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
bubble_sort(nums)
for i in range(len(nums)) :
    print(nums[i], end= " ")
print() 
for i in range(len(nums)) :
    print(nums[len(nums)-i-1], end=" ")