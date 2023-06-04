



N,D = map(int,input().split())



import math

# 2点間の距離
def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


A = []
for i in range(N):
    X,Y = map(int,input().split())
    A.append((X,Y))

from collections import deque

x,y = A[0]
# print(x,y,A)

q = deque()
q.append((x,y))
ans = [0]*N


while q:
    x,y = q.popleft()
    for i in range(N):
        z = get_distance(x,y,A[i][0],A[i][1])
        if ans[i]==0 and z<=D:
            ans[i]=1
            q.append((A[i][0],A[i][1]))
for i in range(N):
    if ans[i]==1:
        print("Yes")
    else:
        print("No")
