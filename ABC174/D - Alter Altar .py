




N,W = map(int,input().split())

A = []
B = []
for i in range(N):
    s,t,p = map(int,input().split())
    A.append((s,p))
    B.append((t,-p))

T = [0] * (11)
print(A)
print(B)
# [(1, 5), (2, 4), (3, 6), (2, 1)]
# [(3, -5), (4, -4), (10, -6), (4, -1)]
for i in range(N):
    x1 = A[i][0]
    y1 = B[i][0]
    x2 = A[i][1]
    y2 = B[i][1]
    T[x1] += x2
    T[y1] += y2
print(T)
from itertools import accumulate
b = list(accumulate(T)) # itertoolsの戻り値はイテレータとなっているので必要に応じてlist化します．
print(b)

for i in b:
    if i>W:
        print("No")
        exit()
print("Yes")





