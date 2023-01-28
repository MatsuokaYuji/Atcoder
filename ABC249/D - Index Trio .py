






# O(NlogK)全探索

N = int(input())


A = list(map(int, input().split()))
from collections import Counter
C = Counter(A)

ans = 0
A_max = 2*10**5

for bunbo in range(1,A_max+1):
    for bunsi in range(bunbo,A_max+1,bunbo):
        k = bunsi//bunbo
        ans+= C[bunbo] * C[bunsi] * C[k]
print(ans)