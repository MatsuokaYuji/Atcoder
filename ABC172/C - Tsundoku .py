








N,M,K = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Aを何冊読むかをiと決めるとBの冊数はN-i


from itertools import accumulate
A_acc = [0] + list(accumulate(A))
B_acc = list(accumulate(B))
# print(A_acc)
# print(B_acc)

# 以下を求める場合right
from bisect import bisect_right

ans = 0

for a in range(N+1):
    asum = A_acc[a]
    tmpK=K-asum
    if tmpK<0:
        break
    b = bisect_right(B_acc,tmpK)
    ans = max(ans,a+b)
print(ans)
