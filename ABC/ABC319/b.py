n = int(input())
ans = ""

for i in range(n+1):
    num = 10
    for j in range(1,10):
        if n%j==0:
            if i%(n/j)==0:
                num = min(num,j)
                break
    if num==10:
        ans += "-"
    else:
        ans += str(num)

print(ans)