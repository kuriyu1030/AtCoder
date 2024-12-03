n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

deli = [-1 for i in range(200005)]

r = 200004

for i in range(n):
    while r >= a[i]:
        deli[r] = i+1
        r -= 1

for i in range(m):
    print(deli[b[i]])