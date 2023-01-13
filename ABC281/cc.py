





n,t = map(int,input().split())

A = list(map(int, input().split()))

S = sum(A)

x = t%S


tmp = 0
num = 0
for i in range(n):
    if A[num] >= x:
        print(num+1,x)
        exit()
    else:
        x -= A[num]
        num+=1
        