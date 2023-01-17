


import math

N = int(input())


def dist(a,b,c,d):
    return math.sqrt((a-c)**2 + (b-d)**2)

p = []

for i in range(N):
    x,y = map(int,input().split())
    p.append([x,y])

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans = max(ans,dist(p[i][0],p[i][1],p[j][0],p[j][1]))
print(ans)
