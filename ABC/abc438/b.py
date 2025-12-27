n, m = map(int, input().split())
s = list(str(input()))
t = list(str(input()))

ans = 10**9

for i in range(n - m + 1):
    c = 0
    for j in range(m):
        s1 = int(s[i + j])
        t1 = int(t[j])
        c += (s1 - t1) % 10
    ans = min(ans, c)

print(ans)