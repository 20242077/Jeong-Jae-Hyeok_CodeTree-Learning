N, M = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]

jewels.sort(key=lambda x: (-x[1]/x[0]))

max_val = 0
for w, v in jewels :
    if w <= M :
        max_val += v
        M -= w
    else :
        max_val += (M/w)*v
        break

print(f"{max_val:.3f}")