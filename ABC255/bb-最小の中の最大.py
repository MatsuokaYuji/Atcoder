



import math


N,K = map(int,input().split())


A = list(map(int, input().split()))

Aplace =[] 

B = []

for i in range(1,N+1):
  x,y = map(int,input().split())
  if i in A:
    Aplace.append((x,y))
  else:
    B.append((x,y))
print(Aplace)

# 各人が照らされるための最小距離を求める、その中での最大値

ans = []
for g in B:
  C = []
  tmp = 10**10
  s = g[0]
  t = g[1]
  for i in Aplace:
    a = math.sqrt((s-i[0]) ** 2 + (t-i[1]) ** 2)
    C.append(a)
  
  ans.append(min(C))

print(max(ans))