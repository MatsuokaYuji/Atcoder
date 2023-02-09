





from bisect import bisect_left,bisect

N,Q = map(int,input().split())
A =list(map(int, input().split()))

C = []

for i in range(1,N+1):
    tp = A[i-1] - i
    C.append(tp)

d = C[N-1]
for _ in range(Q):
    k = int(input())
    i = bisect_left(C,k)
    if i ==0:
        print(k)
    else:
        print(A[i-1] + (k-C[i-1]))


    

    