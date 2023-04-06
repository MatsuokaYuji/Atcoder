









N = int(input())
A = list(map(int, input().split()))
Q = int(input())
from collections import defaultdict
d = defaultdict(int)


for i in range(N):
    x = A[i]
    d[x]+=1

ans = sum(A)

for i in range(Q):
    B,C = map(int,input().split())
    # Bが何回出てきたか
    k = d[B]
    d[B]=0
    d[C]+=k
    ans = ans -(k*B) + (k*C) 
    print(ans)
    
