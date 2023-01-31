

import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

N = int(input())
edges = [ list(map(int, input().split())) for i in range(N-1) ]

# 隣接リストの作成
G = [ list() for i in range(N+1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
	G[a].append(b) # 頂点 a に隣接する頂点として b を追加
	G[b].append(a) # 頂点 b に隣接する頂点として a を追加
for i in range(N+1):
    G[i].sort()
# print(G)

# 深さ優先探索を行う関数（pos は現在位置、pはどこからきたか、
# 今まで訪れた場所じゃなくてついさっきどこからきたのかを持ってれば良い
def dfs(pos,p):
    # 現在位置を追加
    ans.append(pos)
    for v in G[pos]:
        if v!= p:
            dfs(v,pos)
            ans.append(pos)

    
ans = []
# 深さ優先探索
dfs(1,-1)
print(*ans)


