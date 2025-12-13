t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    v = [0 for i in range(2**n)]

    for i, val in enumerate(s):
        if val == "1":
            v[i+1] = -1

    v[0] = 1
    
    for i in range(2**n):
        if v[i]==1:
            for j in range(n):
                if ((i>>j)&1)==0:
                    next = i+2**j
                    if v[next]!=-1:
                        v[next] = 1

    if(v[-1] == 1):
        print("Yes")
    else:
        print("No")