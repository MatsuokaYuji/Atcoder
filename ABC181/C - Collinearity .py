











N = int(input())
L = []

for i in range(N):
    x,y = map(int,input().split())
    L.append((x,y))

L.sort()
# print(L)
from itertools import product, permutations,combinations
A=[i for i in range(N)]
for bit in combinations(A,3):
    # print(bit)
    a = L[bit[0]]
    b = L[bit[1]]
    c = L[bit[2]]
    # print(a,b,c)
    if a[0] == b[0] == c[0]:
        print("Yes")
        exit()
    if a[0] == b[0] or c[0] == b[0] or a[0] == c[0]:
        continue
    s1 = (b[1]-a[1])/ (b[0]-a[0])
    s2 = (c[1]-b[1])/ (c[0]-b[0])
    if s1 ==s2:
        # print(s1,s2)
        # print(a,b,c)
        # print(a[0],a[1])
        # print(b[0],b[1])
        # print(c[0],c[1])
        print("Yes")
        exit()
print("No")
    
