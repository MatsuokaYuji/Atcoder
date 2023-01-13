
from collections import Counter
from itertools import product

N,K = map(int,input().split())


S = [input() for _ in range(N)]

ans = 0

def calc(pro):
    C = Counter()
    for i in range(N):
        if pro[i]:
            for ch in S[i]:
                C[ch] += 1
    score = 0
    for ch,cht in C.items():
        if cht == K:
            score+=1
    return score



for pro in product((True,False),repeat=N):
    ans = max(ans,calc(pro))
print(ans)



# print(C)
# print(pro)

# (True, True, True, True)
# Counter({'a': 3, 'b': 2, 'c': 2, 'i': 1, 'e': 1, 'f': 1, 'g': 1})
# (True, True, True, False)
# Counter({'a': 2, 'b': 2, 'i': 1, 'e': 1, 'f': 1, 'c': 1})
# (True, True, False, True)
# Counter({'a': 3, 'b': 1, 'i': 1, 'e': 1, 'f': 1, 'c': 1, 'g': 1})
# (True, True, False, False)
# Counter({'a': 2, 'b': 1, 'i': 1, 'e': 1, 'f': 1})
# (True, False, True, True)
# Counter({'a': 2, 'b': 2, 'c': 2, 'i': 1, 'g': 1})
# (True, False, True, False)
# Counter({'b': 2, 'a': 1, 'i': 1, 'c': 1})
# (True, False, False, True)
# Counter({'a': 2, 'b': 1, 'i': 1, 'c': 1, 'g': 1})
# (True, False, False, False)
# Counter({'a': 1, 'b': 1, 'i': 1})
# (False, True, True, True)
# Counter({'a': 2, 'c': 2, 'e': 1, 'f': 1, 'b': 1, 'g': 1})
# (False, True, True, False)
# Counter({'a': 1, 'e': 1, 'f': 1, 'b': 1, 'c': 1})
# (False, True, False, True)
# Counter({'a': 2, 'e': 1, 'f': 1, 'c': 1, 'g': 1})
# (False, True, False, False)
# Counter({'a': 1, 'e': 1, 'f': 1})
# (False, False, True, True)
# Counter({'c': 2, 'b': 1, 'a': 1, 'g': 1})
# (False, False, True, False)
# Counter({'b': 1, 'c': 1})
# (False, False, False, True)
# Counter({'a': 1, 'c': 1, 'g': 1})
# (False, False, False, False)
# Counter()
# 3