







from itertools import accumulate


N = int(input())
A = list(map(int, input().split()))

A.sort()
s = A[0]
ans = 0
for i in range(1,N):
    ans+= A[i]*i -s
    s+=A[i]

print(ans)
