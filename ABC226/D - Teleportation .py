



import math
from itertools import product, permutations,combinations

N = int(input())

ans = set()
d = []
for i in range(N):
    x,y = map(int,input().split())
    d.append((x,y))

for p in permutations(d,2):
    print(p)
    t1 = p[0]
    t2 = p[1]
    xs = t1[0]- t2[0]
    ys = t1[1]- t2[1]
    g = math.gcd(xs,ys)
    ans.add((xs//g,ys//g))
print(len(ans))

