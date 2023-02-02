from collections import deque
from heapq import heapify,heappop,heappush

import sys

readline = sys.stdin.readline
Q = int(readline())
S1 = deque()
S2 = []
heapify(S2)
for _ in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        x = query[1]
        S1.append(x)

    elif q == 2:
        if len(S2) == 0:
            print(S1.popleft())
            
        else:
            print(heappop(S2))
    else:  # q == 3
        while S1:
            heappush(S2,S1.popleft())
    