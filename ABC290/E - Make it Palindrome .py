# # 最終手番を考えるとC[0] ==C[n-1]の場合はダメ
# from collections import deque
# t = int(input())
# for _ in range(t):
#     n, m=map(int, input().split())
#     C =list(map(int, input().split()))
#     G = [[] for _ in range(n)]
#     for _ in range(m):
#         u, v=map(int, input().split())
#         G[u-1].append(v-1)
#         G[v-1].append(u-1)
#     if C[0] ==C[n-1]:
#         print(-1)
#         continue
#     d =deque()
#     d.append((0, n-1))
#     dist =[[-1] *n for _ in range(n)]
#     dist[0][n-1] =0
#     while d:
#         taka, ao = d.popleft()
#         for tt in G[taka]:
#             for aa in G[ao]:
#                 if dist[tt][aa] !=-1:
#                     continue
#                 if C[tt]==C[aa]:
#                     continue
#                 dist[tt][aa] =dist[taka][ao] +1
#                 d.append((tt, aa))
#     print(dist[n-1][0])



from collections import deque

t = int(input())

for _ in range(t):
    N,M = map(int,input().split())
    C = list(map(int, input().split()))
    edges = [ list(map(int, input().split())) for i in range(M) ]
    G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
    for a, b in edges:
        a-=1
        b-=1
        G[a].append(b)                      # 頂点 a に隣接する頂点として b を追加
        G[b].append(a)   
    if C[0] == C[N-1]:
        print(-1)
        continue
    d = deque()
    d.append((0,N-1))
    dist = [[-1] * (N) for i in range(N)]
    dist[0][N-1] = 0
    while d:
        taka,ao = d.popleft()
        for tt in G[taka]:
            for aa in G[ao]:
                if dist[tt][aa] !=-1:
                    continue
                if C[tt] == C[aa]:
                    continue
                dist[tt][aa] = dist[taka][ao] + 1
                d.append((tt,aa))
    print(dist[N-1][0]) 

