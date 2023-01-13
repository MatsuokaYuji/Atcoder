

N = int(input())


A = [[0]* (i + 1) for i in range(N)]

for i in range(N):
  for j in range(i+1):
    if j == 0 or j == i:
      A[i][j] = 1
    else:
      A[i][j] = A[i-1][j-1] + A[i-1][j] 
  print(*A[i])



#参考
# combはPython3.8で追加された関数なので、Python3.8で提出してね

from math import comb  
N = int(input())
for i in range(N):
    print(*(comb(i, j) for j in range(i+1)))