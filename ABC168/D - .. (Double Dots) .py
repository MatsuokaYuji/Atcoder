

from collections import deque

# 入力
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for a, b in edges:
	G[a].append(b)
	G[b].append(a)

# bfs
# 幅優先探索の初期化（dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意）
seen = [-1] * (N+1)
seen[1] = 0
ans = [0] * (N+1)
ans[1] = 0

Q = deque()
Q.append(1)


# 幅優先探索
while len(Q) > 0:
    # キュー Q の先頭要素を取り除き、その値を pos に代入する
    pos = Q.popleft()
    for nex in G[pos]:
        if seen[nex] == -1:
            ans[nex] = pos
            seen[nex] =0
            Q.append(nex)

print("Yes")
for i in range(2, N + 1):
	print(ans[i])
