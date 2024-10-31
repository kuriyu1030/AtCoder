n = int(input())
a = list(map(int, input().split()))
deg = [0, 360]

now = 0
for i in a:
    deg.append((now+i)%360)
    now = (now + i)%360

deg.sort()

ans = 0
for i in range(1,len(deg)):
    ans = max(ans, deg[i]-deg[i-1])

print(ans)