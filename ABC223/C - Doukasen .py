

N = int(input())


A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
l = sum(A)
C = []
for i in range(N):
    c = A[i]/B[i]
    C.append(c)

from itertools import accumulate
Csum = list(accumulate(C))
print(Csum)

T = sum(C)/2
print(T)

ans = 0
for i in range(N):
    if Csum[i] <T:
        ans+=A[i]
    else:
        ans+=(T-Csum[i]) * B[i]
print(ans)