













N,Q = map(int,input().split())


A = list(map(int, input().split()))
from collections import defaultdict

graph = defaultdict(list)

for i in range(len(A)):
    graph[A[i]].append(i+1)


for i in range(Q):
    x,k = map(int,input().split())
    if k <=len(graph[x]):
        print(graph[x][k-1])
    else:
        print(-1)




