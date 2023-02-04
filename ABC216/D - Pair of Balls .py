from collections import deque
def topological_sort(G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    q = deque()
    #V: 頂点数
    for i in range(N):
        if into_num[i]==0:
            q.append(i)
    
    #以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす
            if into_num[adj]==0:
                q.append(adj) #入次数が0になったら、キューに入れる
    
    return ans

N,M = map(int,input().split())
G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト

cnt = [0] * N

for _ in range(M):
    k = int(input())
    A = list(map(int, input().split()))
    for i in range(k-1):
        # 有向グラフを作る
        prv = A[i] -1
        nxt = A[i+1] -1
        G[prv].append(nxt)
        # 入次数をカウント
        cnt[nxt] +=1
    
ans = topological_sort(G,cnt)
#  閉路検出
if len(ans) == N:
    print("Yes")
else:
    print("No")