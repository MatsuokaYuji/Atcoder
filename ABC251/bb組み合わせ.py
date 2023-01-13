





N, W = map(int, input().split())

A = list(map(int, input().split()))

import itertools


B = set()

for i in range(1,4):
  for num in itertools.combinations(A,i):
    x = sum(num)
    if x <= W:
      B.add(x)


print(len(B))

# 参考
# from itertools import combinations
 
# N, W = map(int, input().split())
# A = list(map(int, input().split()))
# A.append(0)
# A.append(0)
 
# s = set()
# for i, j, k in combinations(A, 3):
#     if i+j+k <= W:
#         s.add(i+j+k)
 
# print(len(s))