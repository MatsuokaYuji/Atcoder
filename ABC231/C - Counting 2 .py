




from bisect import bisect_left,bisect



N,Q = map(int,input().split())
A = list(map(int, input().split()))

l = len(A)

A.sort()

for i in range(Q):
    x = int(input())
    c = bisect_left(A,x)
    print(l-c)