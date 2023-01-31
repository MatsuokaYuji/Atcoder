





N,M = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
from bisect import bisect_left,bisect


ans = float("INF")
for a in A:
    i = bisect_left(B,a)
    if 1<=i<M+1:
        b1 = B[i-1]
        ans = min(ans,abs(a-b1))
    if 0<=i<M:
        b2 = B[i] 
        ans = min(ans,abs(a-b2))
print(ans)


