





N, M = map(int, input().split())
A = list(map(int, input().split()))

edges = [ list(map(int, input().split())) for i in range(M) ]

G = [ list() for i in range(N) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

ans=0
for i,g in enumerate(G):
    x = A[i]
    flag = True
    for v in g:
        y = A[v]
        if x<=y:
            flag = False
            break
    if flag:
        ans+=1
print(ans)

