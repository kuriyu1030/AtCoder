h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

sum_h = [sum(row) for row in a]

sum_w = [sum(col) for col in zip(*a)]

b = [[sum_h[i]+sum_w[j]-a[i][j] for j in range(w)] for i in range(h)]

for row in b:
    print(*row)