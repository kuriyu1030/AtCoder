n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ans = 10**10
a_i = 0

for i in range(m):
    if a_i == n:
        print(ans)
        exit()

    if b[i] >= a[a_i]:
        ans = min(abs(a[a_i] - b[i]), ans)
        if i != 0:
            ans = min(ans, abs(a[a_i] - b[i-1]))
        a_i += 1
        while a_i != n and b[i] >= a[a_i]:
            if b[i] >= a[a_i]:
                ans = min(abs(a[a_i] - b[i]), ans)
                if i != 0:
                    ans = min(ans, abs(a[a_i] - b[i-1]))
            a_i += 1

if ans == 10**10:
    ans = abs(b[-1] - a[0])

print(ans)