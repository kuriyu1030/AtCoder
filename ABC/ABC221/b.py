s = str(input())
t = str(input())

ans = "No"
if s == t:
    ans = "Yes"

for i in range(len(s)-1):
    test = s[0:i] + s[i+1:i+2] + s[i:i+1] + s[i+2:]
    if test == t:
        ans = "Yes"

print(ans)