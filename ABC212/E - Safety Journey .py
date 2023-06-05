

MOD = 998244353

N,M,K = map(int,input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

dp = [[0]* N for i in range(K+1)]
dp[0][0] = 1

# K日間
for i in range(1,K+1):
    pre_sum = sum(dp[i-1])
    for j in range(N):
        # K-1日目の合計
        dp[i][j] += pre_sum
        # 同じ場所からの移動はひく
        dp[i][j] -= dp[i-1][j]
        dp[i][j] %= MOD
        # 閉じている道の分を引く
        for k in G[j]:
            dp[i][j] -= dp[i-1][k]
            dp[i][j] %= MOD
print(dp[K][0] % MOD)
