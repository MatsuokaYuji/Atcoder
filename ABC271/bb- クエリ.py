







N,Q= map(int,input().split())

A = [list(map(int, input().split())) for _ in range(N)]
# print(A[0])


for i in range(Q):
    s,t = map(int,input().split())
    print(A[s-1][t])