n, d = map(int, input().split())
s = str(input())

print(min(s.count(".") + d, n))