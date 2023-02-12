




from collections import deque


N,M = map(int,input().split())

a = (-10)**3
b = (10)**3
myaku = []
for i in range(a,b):
    for j in range(a,b):
        if M == i**2+j**2:
            myaku.append((i,j))
# print(myaku)
# myaku = [(1,0),(0,1),(-1,0),(0,-1)]

d = deque()
d.append((0,0))
dist = [[-1] * (N) for i in range(N)]
dist[0][0] = 0
while d:
    x,y = d.popleft()
    for i,j in myaku:
        # print(i,j)
        # print(x+i,y+j)
        if x+i>=N or y+j >=N or  x+i<0 or y+j <0:
            continue
        if dist[x+i][y+j] ==-1:
            dist[x+i][y+j] = dist[x][y] + 1
            d.append((x+i,y+j))
            continue
        if dist[x+i][y+j] >dist[x][y] + 1:
            continue
        
    
for i in range(N):
    print(*dist[i]) 