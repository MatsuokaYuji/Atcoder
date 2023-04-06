









N = int(input())
A = list(map(int, input().split()))

ans = 0
from collections import Counter
C=Counter(A)

s =set(A)
m= 10**6+1
cnt = [0] * (m)

for a in s:
    # 倍数を考える調和級数っぽい形になるので、O(NlogN)になり間に合う
    for i in range(2*a,m,a):
        cnt[i]+=1

for a in s:
    # 出現回数が2回以上のやつは無条件にアウト
    if cnt[a]==0 and C[a] ==1:
        ans+=1
print(ans)
