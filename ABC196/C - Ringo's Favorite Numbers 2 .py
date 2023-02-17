
# def factorial_for(num):
#     val = 1
#     for i in range(num, 1, -1):
#         val *= i
#     return val

import math
N = int(input())

A = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(int)

for i in range(N):
    x = A[i]%200
    d[x]+=1
ans = 0
for i in range(200):
    if d[i] == 0 or d[i] == 1:
        continue
    z = math.comb(d[i], 2)
    ans+=z

print(ans)
