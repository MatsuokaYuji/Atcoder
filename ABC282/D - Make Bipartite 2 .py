

# グラフの連結成分のうち、まだ考えていない連結成分について、1 つの頂点を選んで「白色」に塗る (黒色でもよい)
# その頂点とつながる頂点に対しては、次々と連鎖的に色が決まっていく
# その決まった色が整合性を取れない場合は二部グラフではない
# 以上の作業を、連結成分がなくなるまで繰り返す
# 余事象の考え方
# 連結成分間を結ぶ場合、異なる連結成分間

# 具体的には、同じ連結成分内の白色頂点の個数を a、黒色頂点の個数を b としたとき、
# 結んではいけない辺の本数は
# a(a−1)//2+b(b−1)//2
# と表せる。これを各連結成分について合算すればよい。

# 全体として、計算量は O(N+M) となる。

# 毛チョン解法
import queue
from collections import deque


def com(n):
    return n * (n-1)//2

white,black = 0,1

N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

G = [ list() for i in range(N+1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
	G[a].append(b)                      # 頂点 a に隣接する頂点として b を追加
	G[b].append(a)                      # 頂点 b に隣接する頂点として a を追加

num_ng_edges = 0
is_bipartite = True
color = [-1] * (N+1)

for s in range(N):
    # 探索ずみなら次
    if color[s] !=-1:continue
    # その連結成分での白色、黒色の個数
    white_num,black_num = 0,0
    que = deque()
    que.appendleft(s)
    color[s] = white
    while que:
        v = que.popleft()
        if color[v] == white: white_num+=1
        else:black_num+=1
        for v2 in G[v]:
            # すでに色が塗られている場合
            if color[v2] !=-1:
                # 隣接が同色なら二部グラフじゃない
                if color[v2] == color[v]:
                    is_bipartite = False
            else:
                color[v2] = 1-color[v]
                que.appendleft(v2)
    num_ng_edges += com(white_num) + com(black_num)

print(com(N) - M - num_ng_edges if is_bipartite else 0)
