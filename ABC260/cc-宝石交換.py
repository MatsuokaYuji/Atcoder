


N,X,Y = map(int,input().split())


A = [0] * (N+1)
B = [0] * (N+1)

A[N] = 1

def red(n):
    if n == 1:
        return 
    A[n-1] += A[n]
    B[n] += A[n] * X 
    return 

def blue(n):
    if n == 1:
        return
    A[n-1] += B[n]
    B[n-1] += B[n] * Y  
    return 

for i in range(N,-1,-1):
    red(i)
    blue(i)
print(B[1])
