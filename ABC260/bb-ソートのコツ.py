




N,X,Y,Z = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []

P = []
for i in range(N):
    P.append([A[i],-(i+1)])

P.sort(reverse=True)


for i in range(X):
    ans.append(-P[i][1])

EngP = []

for i in range(N):
    if (i+1) not in ans:
        EngP.append([B[i],-(i+1)])

EngP.sort(reverse=True)

for i in range(Y):
    ans.append(-EngP[i][1])

sumAB = []

for i in range(N):
    if (i+1) not in ans:
        sumAB.append([A[i]+B[i],-(i+1)])

sumAB.sort(reverse=True)

for i in range(Z):
    ans.append(-sumAB[i][1])

ans.sort()
for i in ans:
    print(i)