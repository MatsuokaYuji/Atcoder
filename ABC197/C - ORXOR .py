






N = int(input())
A = list(map(int, input().split()))

# 全探索可能 2**(N-1)<=1048576
# N * (2**N)で間に合う

from itertools import product, permutations,combinations
ans = float('INF')
for bit in product((True, False), repeat=N - 1):
    # 番兵追加
    bit = list(bit) + [True]
    # print(bit)
    now = 0
    score = 0
    for i in range(N):
        now |= A[i]
        if bit[i]:
            score^=now
            now = 0
    ans = min(ans,score)
print(ans)