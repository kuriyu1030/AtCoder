d, f = map(int, input().split())
ans = (f-d)%7
print(7 if ans == 0 else ans)