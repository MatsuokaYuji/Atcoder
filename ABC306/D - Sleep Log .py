
# [0, 240, 720, 1320, 1440, 1800, 2160]
# [0, 720, 1440, 2160]
# 2 6
# 2 3
# 0 6

N = int(input())
A = list(map(int, input().split()))
# print(A)
d = []
for i in range(0,(N-1)//2 +1):
    d.append(A[2*i])
# print(d)
B = [0] * len(d)
for i in range(2,N):
    if i%2==0:
        B[i//2] = A[i] -A[i-1]
# print(B)
from itertools import accumulate
C = list(accumulate(B))
# print(C)


Q = int(input())
from bisect import bisect_left,bisect

for i in range(Q):
    ans = 0
    l,r = map(int,input().split())
    dl = bisect_left(A,l)
    dr = bisect_left(A,r)
    a,b = dl//2,dr//2
    ans+= C[b]
    ans-= C[a]

    if dl %2==0:
        ans += A[dl]-l
    # else:
    #     ans += A[dl]- A[dl-1]

    if dr%2==0:
        ans -= (A[dr] - r)

    # else:
    #     ans += l-
    
        
    # print(l,r,i)
    # print(dl,dr)
    print(ans)


