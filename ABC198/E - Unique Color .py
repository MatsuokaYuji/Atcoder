
import sys
sys.setrecursionlimit(10 ** 5)  # 再帰上限を大きくしないとREになります


from collections import Counter

# 入力
N = int(input())
C = [-1] + list(map(int, input().split()))

edges = [list(map(int, input().split())) for i in range(N-1)]

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)
# print(G)
good = [False] * (N+1)

# 色を管理する掲示板があるイメージ
color_count = Counter()

def dfs(pos,parent):
    color = C[pos]
    if color_count[color] == 0:
        good[pos] = True
    color_count[color] +=1
    for v in G[pos]:
        if v == parent:
            continue
        dfs(v,pos)
    # 戻る時にカウント減らす
    color_count[color] -=1
dfs(1,-1)

for i in range(len(good)):
    if good[i]:
        print(i)
