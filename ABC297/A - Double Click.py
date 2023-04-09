

N,D = map(int,input().split())
A = list(map(int, input().split()))


for i in range(N-1):
    x = A[i+1]-A[i]
    if x<=D:
        print(A[i+1])
        exit()
print(-1)