n = int(input())
name = set()

for i in range(n):
    s = str(input())
    if not(s in name):
        print(i+1)
        name.add(s)