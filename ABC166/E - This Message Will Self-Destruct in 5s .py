











N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(int)


ans=0
for i in range(N):
    ans+=d[i-A[i]]
    b = i+A[i]
    d[b]+=1
print(ans)
