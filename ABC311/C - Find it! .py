



N = int(input())

A = list(map(int, input().split()))

seen = [0]*N

G = [ list() for i in range(N) ] # G[i] は頂点 i に隣接する頂点のリスト
for i in range(N):
    a = A[i]-1
    G[i].append(a)
    G[a].append(i)

from collections import deque
q = deque([0])
seen[0] = 1
ans = [0]

while q:
    v = q.pop()
    for g in G[v]:
        if seen[v]:
            d = ans.index(g+1)
            print(len(ans[d:]))
            print(*ans[d])
        else:
            seen[v] = 1
            ans.append(g+1)
            q.append(g)




