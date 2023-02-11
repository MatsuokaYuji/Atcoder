


N,M = map(int,input().split())

from itertools import product, permutations,combinations

p = 2**M-1

S = []
for i in range(M):
	C = int(input())
	A = list(map(int, input().split()))
	S.append(A)

B = []
for i in S:
    tmp = set(i)
    B.append(tmp)
# [{1, 2}, {1, 3}, {2}]

ans = 0
for a in product(range(2), repeat=M):
	tmp = set()
	for i in range(M):
		if a[i] ==1:
		    for k in B[i]:
			    tmp.add(k)
if len(tmp) == N:
		ans+=1
print(ans)	


