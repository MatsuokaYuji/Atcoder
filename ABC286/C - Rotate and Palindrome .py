







N,A,B = map(int,input().split())
S = input()
from collections import deque

S = list(S)
S = deque(S)
ans = 10**15
for a in range(N):
	b =0
	for k in range(N//2):
		if S[k]!=S[N-1-k]:
			b+=1
	ans = min(ans,a*A+b*B)
	f =S.popleft()
	S.append(f)
print(ans)

