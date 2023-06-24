
from itertools import product


N = int(input())
nodes = []
for _ in range(N):
    nodes.append(list(map(int, input().split())))

def dist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# Sの値を二ぶ探索
# 今回Sは単調増加、条件を満たすSの強化位置を求めたい
def nibutan(start,end,ans):
    ng = start
    ok = end
    while ng!=ok:
        p=(ng+ok+1)//2
        result = ans(p)
        if result:
            ng = p
        else:
            ok = p-1
    return ng

def ans(S):
    edges = [[None for j in range(N)] for i in range(N)]
    # 有向辺をはる
    for i,j in product(range(N),range(N)):
        d = dist((nodes[i][0], nodes[i][1]), (nodes[j][0], nodes[j][1]))
        if d <= S * nodes[i][2]: 
            edges[i][j] = 1
    
    # 連結しているものにチェック?
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if edges[i][k] and edges[k][j]:
                    edges[i][j] = 1
    
    # 全ての辺が連結ならTrue
    for i in range(N):
        for j in range(N):
            if edges[i][j] is None:
                break
        else: return False
    else: return True
    
print(nibutan(0, 4 * 10 ** 9 + 1, ans) + 1)





# import math

# N = int(input())
# G = []
# for _ in range(N):
#     x, y, p = map(int, input().split())
#     G.append([x, y, p])

# dist = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         d = abs(G[i][0] - G[j][0]) + abs(G[i][1] - G[j][1])
#         dist[i][j] = math.ceil((d + G[i][2] - 1) // G[i][2])
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))
# ans = 10**18
# for d in dist:
#     cnt = max(d)
#     ans = min(ans, cnt)
# print(ans)