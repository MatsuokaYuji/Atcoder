



h1,w1 = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h1)]
h2,w2 = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(h2)]

from itertools import combinations
iter1 = list(combinations(range(h1),h2))
iter2 = list(combinations(range(w1),w2))

def check(i1,i2):
    for x,h in enumerate(i1):
        for y,w in enumerate(i2):
            if A[h][w] != B[x][y]:
                return False
    return True

satisfied = False
for i1 in iter1:
    if satisfied == True:
        break

    for i2 in iter2:
        if check(i1,i2):
            satisfied = True
            break

if satisfied == True:
    print("Yes")
else:
    print("No")