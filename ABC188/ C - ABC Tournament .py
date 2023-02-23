









N = int(input())
A = list(map(int, input().split()))

if N==1:
    if A[0]<A[1]:
        print(1)
        exit()
    else:
        print(2)
        exit()
from heapq import heapify,heappop,heappush

L = list(range(2**N))
heapify(L)

# print(L)
while len(L) >1:
    tmp = set()
    for i in range(len(L)//2):
        x = heappop(L)
        y = heappop(L)
        if A[x] <A[y]:
            tmp.add(y)
        else:
            tmp.add(x)
    if len(tmp)==1:
        if A[x] <A[y]:
            print(x+1)
        else:
            print(y+1)
    for i in tmp:
        heappush(L,i)

