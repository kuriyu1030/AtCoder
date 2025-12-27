n = int(input())
a = list(map(int, input().split()))

stack = []

for x in a:
    if len(stack)>0 and stack[-1][0] == x:
        stack[-1][1] += 1
        if stack[-1][1] == 4:
            stack.pop()
    else:
        stack.append([x, 1])

ans = sum(cnt for val, cnt in stack)
print(ans)