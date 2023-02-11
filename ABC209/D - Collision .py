


from collections import deque

# 入力
N, Q = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(N-1) ]

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for a, b in edges:
	G[a].append(b)
	G[b].append(a)


# 幅優先探索の初期化（dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意）
visited = [False] * (N+1)
visited[1] = 0
colors = [-1] * (N+1)
Q = deque()
Q.append(1)
colors[1] = 0


# 幅優先探索
while len(Q) > 0:
    # キュー Q の先頭要素を取り除き、その値を pos に代入する
    pos = Q.popleft()
    for nex in G[pos]:
        if visited[nex] == False:
            visited[nex] = True
            colors[nex] = 1-colors[pos]
            Q.append(nex)

# 頂点 1 から各頂点までの最短距離を出力
for i in range(Q):
    c,d = map(int,input().split())
    if colors[c] == colors[d]:
        print("Town")
    else:
        print("Road")

	