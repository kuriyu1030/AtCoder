h, w, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

for i in range(n):
    b = int(input())
    for n1 in range(h):
        for n2 in range(w):
            if b == a[n1][n2]:
                a[n1][n2] = -1
                
ans = []

for n1 in range(h):
    ans.append(a[n1].count(-1))

print(max(ans))