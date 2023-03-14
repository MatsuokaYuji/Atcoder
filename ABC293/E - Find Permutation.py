from collections import deque
def topological_sort(G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    q=deque()
    #V: 頂点数
    # 入次数が0のやつを小さい順に詰め込んでいく
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
                q.append(adj)
    
    return ans

N,M = map(int,input().split())
G = [ list() for i in range(N) ] # G[i] は頂点 i に隣接する頂点のリスト

cnt = [0] * N
for _ in range(M):
    a,b = map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    # 入次数をカウント
    cnt[b] +=1
    
ans = topological_sort(G,cnt)


# print(ans)
if len(ans) <N:
  print("No")
  exit()
# 最長passの長さを求めているこれがN-1ならだめ
dp = [0]*N
for p in ans:
    for d in G[p]:
        dp[d] = max(dp[d],dp[p]+1)
# print(dp)
# print(max(dp))
if max(dp)<N-1:
    print("No")
    exit()
print("Yes")
ret = [0]*N
for i in range(N):
    ret[i] = dp[i]+1
print(*ret)

