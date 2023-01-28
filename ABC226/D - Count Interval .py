


from collections import Counter

N,K = map(int,input().split())


A = list(map(int, input().split()))

from itertools import accumulate
B = list(accumulate(A))

C = Counter()

C[0] +=1
# 連続部分列の0番目からi番目を数えるために、0を1個入れる必要があります

ans = 0

for x in B:
    # x - y = K より、y = x - K である連続部分列が今まで何回出てきたかが知りたいものです
    y = x-K
    ans+= C[y]
    C[x] +=1
    
print(ans)