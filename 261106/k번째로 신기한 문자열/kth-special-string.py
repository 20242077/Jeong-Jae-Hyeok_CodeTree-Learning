n, k, t = input().split()
n, k = int(n), int(k)
words = [input() for _ in range(n)]

arr = []
for word in words:
    if word.startswith(t):
        arr.append(word)

arr.sort()
print(arr[k-1])