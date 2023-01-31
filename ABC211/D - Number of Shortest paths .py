

from collections import deque

# 入力
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for a, b in edges:
	G[a-1].append(b-1)
	G[b-1].append(a-1)


INF = 1<<60
MOD  = 10**9 +7
dist = [INF] * N
dist[0] = 0
dp = [0] * N
dp[0] = 1

Q = deque((0,))

# 幅優先探索
while len(Q) > 0:
    # キュー Q の先頭要素を取り除き、その値を pos に代入する
    pos = Q.popleft()
    curr_cost = dist[pos]
    next_cost = curr_cost + 1
    for v in G[pos]:
        if next_cost < dist[v]:
            Q.append(v)
            dist[v] = next_cost
        if next_cost == dist[v]:
            dp[v]+=dp[pos]
            dp[v]%=MOD

print(dp[-1])
