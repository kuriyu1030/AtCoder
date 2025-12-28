n = int(input())
test = [(0, 0)]

for i in range(n):
    c, p = map(int, input().split())
    test.append((test[i][0] + p, test[i][1]) if c==1 else (test[i][0], test[i][1] + p))

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(test[r][0]-test[l-1][0], test[r][1]-test[l-1][1])