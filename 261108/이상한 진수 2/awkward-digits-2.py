a = input()
n = len(a)
N = list(a)
maxval = 0
for i in range(n) :
    N[i] = str(1-int(N[i]))
    maxval = max(maxval, int(''.join(N), 2))
    N[i] = str(1-int(N[i]))
    
print(maxval)