




N,M,X,T,D = map(int,input().split())


for i in range(N,X,-1):
    if i == M:
        print(T)
        exit()

for i in range(X,-1,-1):
    if i == M:
        print(T)
        exit()
    T = T-D