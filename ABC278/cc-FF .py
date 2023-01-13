









# 入力の受け取り
N,Q = map(int,input().split())
from collections import defaultdict

Follow = defaultdict(int)

for i in range(Q):
    T,a,b = map(int,input().split())
    if T == 1:
       Follow[(a,b)] = 1
    if T== 2:
        Follow[(a,b)] = 0
    if T== 3:
        if Follow[(a,b)] == 1 and Follow[(b,a)] == 1:
            print("Yes")
        else:
            print("No")


