





N,K = map(int,input().split())
A = list(map(int, input().split()))
from collections import Counter
C = Counter(A[:K])
ans = len(C)
for i in range(K,N):
    left = A[i-K]
    right = A[i]
    C[left] -=1
    C[right] +=1
    if C[left] == 0:
        del C[left]
    ans = max(ans,len(C))
    

print(ans)