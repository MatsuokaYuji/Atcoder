
from collections import defaultdict
d = defaultdict(int)

N = int(input())

A = list(map(int, input().split()))

all = 0

Q = int(input())

for i in range(N):
  d[i] = A[i]

for i in range(Q):
  query = list(map(int, input().split()))
  q = query[0]
  if q == 1:
    all=query[1]
    d = defaultdict(int)
  if q == 2:
    d[query[1]-1] += query[2]
  if q == 3:
      ans = all + d[query[1]-1]
      print(ans)
      
  


