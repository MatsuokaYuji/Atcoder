

import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

N, Q = map(int, input().split())
X = [0] + list(map(int, input().split()))

edges = [ list(map(int, input().split())) for i in range(N-1) ]

# 隣接リストの作成
G = [ list() for i in range(N+1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
	G[a].append(b) # 頂点 a に隣接する頂点として b を追加
	G[b].append(a) # 頂点 b に隣接する頂点として a を追加

L = [[] for i in range(N+1)]

# 深さ優先探索を行う関数（pos は現在位置、pはどこからきたか、
# 今まで訪れた場所じゃなくてついさっきどこからきたのかを持ってれば良い
def dfs(u,p):
    # 現在位置を追加
    L[u].append(X[u])
    for v in G[u]:
        if v == p:
            continue
        dfs(v,u)
        L[u].extend(L[v])
    L[u].sort(reverse=True)
    L[u] = L[u][:20]


dfs(1,0) 

for i in range(Q):
    v,k= map(int,input().split())
    print(L[v][k-1])
