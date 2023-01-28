

N = int(input())
def calc (ax,bx,cx,ay,by,cy):
    d1 = (by-ay) * (cx-ax)
    d2 = (cy-ay) * (bx-ax)
    if d1==d2:
        return False
    return True


P= []
for i in range(N):
    x,y = map(int,input().split())
    P.append([x,y])
from itertools import product, permutations,combinations
ans=0
for a,b,c in combinations(P, 3):
    # print(a,b,c)
    if calc(a[0],b[0],c[0],a[1],b[1],c[1]):
        ans+=1
print(ans)
