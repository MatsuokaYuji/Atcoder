N=int(input())
graph = {}
chk={}
arr=[]

for _ in range(N):
    S, T = map(str, input().split())
    graph[S]=T
    chk[S]=False
    arr.append(S)

def chk_loop(S):
    now=S
    while True:
        chk[now]=True
        if graph[now] not in graph:
            return True
        elif graph[now]==S:
            return False
        else:
            now=graph[now]

for i in arr:
    if not chk[i]:
        if not chk_loop(i):
            exit(print('No'))
print('Yes')

