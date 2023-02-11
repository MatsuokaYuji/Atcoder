



N,K = map(int,input().split())
A = list(map(int, input().split()))


all = 0

if K>=N:
    d = K//N

    all+=d
    K-=d* N
from collections import defaultdict
d = defaultdict(int)

for i in range(N):
    d[A[i]] +=all
B = sorted(A)

for i in range(K):
    d[B[i]] +=1


for i in A:
    print(d[i])