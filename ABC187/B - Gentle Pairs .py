
import math


def get_kata(x1, y1, x2, y2):
    d = (y2-y1)/(x2-x1)
    return d

N = int(input())


L = []

for i in range(N):
    x,y = map(int,input().split())
    L.append((x,y))

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        x1,y1 = L[i][0],L[i][1]
        x2,y2 = L[j][0],L[j][1]
        d = get_kata(x1,y1,x2,y2)
        if -1<=d<=1:
            ans+=1
print(ans)