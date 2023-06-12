








# bfs、BFS、多始点
N,M,K = map(int,input().split())


edges = [ list(map(int, input().split())) for i in range(M) ]

# G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
G = [ set() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
    
    G[a].add(b)
    G[b].add(a)

from heapq import heapify,heappop,heappush
q = []
ans = set()
for i in range(K):
    p,h = map(int,input().split())
    # 最大値からみるために-でpushしていく
    q.append((-h,p))
    ans.add(p)
heapify(q)

seen = [False] * (N+1)


while q:
    h,p = heappop(q)
    if h==0:
        continue
    # 最大値からみていく
    h = -h
    h-=1
    for v in G[p]:
        if seen[v]:
            continue
        seen[v] = True
        ans.add(v)
        heappush(q,(-h,v))
print(len(ans))
# print(*ans)
# こう書かないとエラー
print(*sorted(list(ans)))
