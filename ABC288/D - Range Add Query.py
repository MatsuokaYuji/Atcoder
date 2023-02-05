





N,K = map(int,input().split())

A = list(map(int, input().split()))

Q = int(input())
from itertools import accumulate
b = list(accumulate(A))
for e in range(Q):
    l,r = map(int,input().split())
    n = l-r+1
    x = A[l:r+1]
    g = len(x)
    i = 1
    while True:    
        c = x[-i]
        if i==g and x[0]!=0:
            print("No")
            exit()
        if i==g and x[0]==0:
            print("Yes")
            exit()
        if c == 0:
            i+=1
            continue
        for j in range(n-K-1):
            x[j + i + (n-K-1) - 1] -=c

    

