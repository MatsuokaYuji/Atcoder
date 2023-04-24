



# 後でテストケース確認 041のケース

# すべての i=1,2,…,K について、下記の条件が成り立つ。
# 頂点 piから距離がdi未満の頂点はすべて白で塗る


N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

from collections import deque

K = int(input())

# 初期値1,0なら白、1なら黒
ans = [-1]*(N)
# print(G)
for i in range(K):
    # print("何周目",i)
    p,d = map(int,input().split())
    p-=1
    q = deque()
    # 頂点iと距離
    q.append((p,1))
    seen = [0]*N
    if d!=0:
        ans[p] = 0
        seen[p] = 1
    # これ追加で 034消えた
    if d==0:
        if ans[p]==0:
            print("No")
            exit()
        ans[p]=1
        continue
    while q:
        V,dist = q.popleft()
        # print(V,dist)
        for v in G[V]:
            # 今見ている頂点からの距離distがd未満か否か
            if seen[v]==1:
                continue
            seen[v]=1
            if dist<d:
                ans[v] = 0
                q.append((v,dist+1))
                # print(v,dist,"change")
            elif dist==d:
                if ans[v]==-1:
                    ans[v] = 1
            else:
                break
for i in range(N):
    if ans[i]==-1:
        ans[i]=1
if sum(ans)!=0:
    print("Yes")
    # for i in range(N):
    #     print(ans[i],end="")
    print(*ans, sep='')
else:
    print("No")
    




# from collections import deque
# from collections import defaultdict

# n, m = map(int, input().split())
# edge = [[] for _ in range(n)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     u -= 1
#     v -= 1
#     edge[u].append(v)
#     edge[v].append(u)

# # 白を先に確定させる
# # 残った色はすべて黒にする
# # 最後に条件を満たしているか判定

# k = int(input())
# conditions = []
# for _ in range(k):
#     p, d = map(int, input().split())
#     conditions.append((p - 1, d))

# # 黒で初期化
# color = [1 for _ in range(n)]

# # 白を確定させていく＆距離dの頂点を保持
# dict = defaultdict(list)
# for condition in conditions:
#     p, d = condition

#     # 幅優先探索
#     q = deque()
#     q.append((p, 0))
#     visited = [False for _ in range(n)]
#     while len(q) > 0:
#         current, dist = q.popleft()
#         if visited[current]:
#             continue
#         visited[current] = True
#         if dist == d:
#             dict[p].append(current)
#         if dist > d:
#             break
#         if dist < d:
#             color[current] = 0
#             for nxt in edge[current]:
#                 q.append((nxt, dist + 1))

# # 条件を満たしているか判定
# for node, _ in conditions:
#     satisfied = False
#     for candidate in dict[node]:
#         if color[candidate] == 1:
#             satisfied = True
#     if not satisfied:
#         print('No')
#         exit()

# print('Yes')
# print(*color, sep='')
