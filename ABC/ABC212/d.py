from heapq import heapify, heappop, heappush

q = int(input())
val = 0
ball = []

for i in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        heappush(ball, que[1] - val)
    elif que[0] == 2:
        val += que[1]
    else:
        print(heappop(ball) + val)