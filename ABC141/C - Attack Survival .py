




N,K,Q = map(int,input().split())
from collections import defaultdict
d = defaultdict(int)

for i in range(Q):
	A = int(input())
	d[A] +=1
for i in range(1,N+1):
	if K-Q+d[i]>=1:
		print("Yes")
	else:
		print("No")
