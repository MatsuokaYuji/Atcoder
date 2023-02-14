from collections import deque
def topological_sort(G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    L = []
    heapify(L)
    #V: 頂点数
    # 入次数が0のやつを小さい順に詰め込んでいく
    for i in range(1,N+1):
        if into_num[i]==0:
            heappush(L,i)
    
    #以下、幅優先探索
    ans = []
    while len(L)>0:
        v = heappop(L)
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす
            if into_num[adj]==0:
                heappush(L,adj) #入次数が0になったら、キューに入れる
    
    return ans

# 辞書順に小さいのは貪欲法、
# 使える数字を管理して小さいものから取り出すので、優先度付きキュー
# Biとして現れる回数を各頂点で記録、そのカウントが0になったやつはキューにいれる
# トポロジカルソートのキューを優先度付きに変えたver


from heapq import heapify,heappop,heappush

N,M = map(int,input().split())
G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト

cnt = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    # 入次数をカウント
    cnt[b] +=1
    
ans = topological_sort(G,cnt)
#  閉路検出
if len(ans) == N:
    print(*ans)
else:
    print(-1)