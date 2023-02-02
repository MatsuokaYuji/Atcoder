

N = int(input())

from collections import defaultdict
d = defaultdict(int)

points = []


for i in range(N):
    A,B = map(int,input().split())
    points.append([A,B])
    d[(A,B)] =1

# print(points)
# print(d)

ans = 0

for p1 in range(N):
    for p2 in range(p1+1,N):
        x1,y1 = points[p1]
        x2,y2 = points[p2]
        if x1 == x2 or y1 == y2:
            continue
        # mapで存在確認することではやく
        if d[(x1,y2)] == 1 and d[(x2,y1)] == 1:
            ans+=1
ans//=2
print(ans)