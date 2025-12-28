import math
a, b, c = map(int, input().split())
num = math.gcd(a, b, c)
print((a+b+c)//num-3)