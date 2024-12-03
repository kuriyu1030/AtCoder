s = str(input())

ans1 = True
ans2 = True

for i in range(4):
    if s[0] != s[i]:
        ans1 = False

for i in range(1,4):
    if ((ord(s[i-1]) - ord('0')) + 1) % 10 != (ord(s[i]) - ord('0')):
        ans2 = False

if ans1 or ans2:
    print("Weak")
else:
    print("Strong")