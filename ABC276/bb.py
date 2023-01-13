



n,m = map(int,input().split())


A = [[] for i in range(n)]


for i in range(m):
    a,b = list(map(int, input().split()))
    A[a-1].append(b)
    A[b-1].append(a)
# [[3, 2, 6], [5, 1], [6, 1], [], [6, 2], [3, 5, 1]]

for i in range(n):
    l = len(A[i])
    A[i].sort()
    if l == 0:
        print(0)
        continue
    print(l,end=" ")
    for j in range(l-1):
        print(A[i][j],end=" ")
    print(A[i][l-1])