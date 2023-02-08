

from collections import deque

# 入力
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for a, b in edges:
	G[a].append(b)
# print(G)
ans = 0
for i in range(1,N+1):
    # 幅優先探索の初期化（dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意）
    visited =[False] * (N + 2)

    Q = deque()
    Q.append(i)

    tmpans = 1
    visited[i] = True
    # 幅優先探索
    while len(Q) > 0:
        # キュー Q の先頭要素を取り除き、その値を pos に代入する
        pos = Q.popleft()
        for nex in G[pos]:
            if not visited[nex]:
                visited[nex] = True
                tmpans+=1
                Q.append(nex)
    ans+=tmpans
    # print(tmpans)
print(ans)