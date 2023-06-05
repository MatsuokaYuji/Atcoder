









H,W,M = map(int,input().split())

cnth = [0] * H
cntw = [0] * W 

from collections import defaultdict
d = defaultdict(int)

for i in range(M):
    h,w = map(int,input().split())
    cnth[h-1] +=1
    cntw[w-1] +=1
    d[(h-1,w-1)] +=1


max_h = max(cnth)
max_w = max(cntw)

mh = []
mw = []

# 候補を炙り出す
for i in range(H):
    if max_h == cnth[i]:
        mh.append(i)

for i in range(W):
    if max_w == cntw[i]:
        mw.append(i)

for i in mh:
    for j in mw:
        if d[(i,j)] == 0:
            print(max_h + max_w)
            exit()
print(max_h + max_w-1)