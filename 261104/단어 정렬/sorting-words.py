n = int(input())
word = [input() for _ in range(n)]
arr = list(word)
arrSorted = sorted(arr)
for i in range(len(arrSorted)) :
    print(arrSorted[i])
# Please write your code here.