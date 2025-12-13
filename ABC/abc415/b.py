s = list(input())
index = [i for i, ch in enumerate(s) if ch=="#"]

for i in range(0, len(index), 2):
    print(f"{index[i]+1},{index[i+1]+1}")