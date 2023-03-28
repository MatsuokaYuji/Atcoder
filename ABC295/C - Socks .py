






N = int(input())
A = list(map(int, input().split()))
from collections import Counter
C=Counter(A)
# print(C)
d = C.most_common()
ans = 0
for i,j in d:
    if j>=2:
        tmp = j//2
        ans+=tmp
    else:
        print(ans)
        exit()
    # print(i,j)
print(ans)


