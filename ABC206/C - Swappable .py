


N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(int)

for i in range(N):
    d[A[i]] +=1

l = len(A)-1
ans = 0
for i in range(N):
    tmp = l-d[A[i]] +1
    if d[A[i]] >=2:
        d[A[i]] -=1
    ans+=tmp
    l-=1
print(ans)
