n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

ans = a[0:p-1] + a[r-1:s] + a[q:r-1] + a[p-1:q] + a[s:]
print(" ".join(map(str, ans)))