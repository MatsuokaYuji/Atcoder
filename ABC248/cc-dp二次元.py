




N, M, K = map(int, input().split())

MOD = 998244353

# Aの合計がK以下でかつ、Aのそれぞれの要素はM以下
dp = [ [ 0 ] * (K + 1) for i in range(N + 1) ]

dp[0][0] = 1
# dp[i][j] 項数がiで総和がjの組み合わせ数
# dp[i+1][j+k] += dp[i][j]   1<=k<=M

for i in range(N):
    for j in range(K):
        for k in range(1,M+1):
            if j+k> K:
                break
            dp[i+1][j+k] += dp[i][j]
            dp[i+1][j+k] %= MOD
print(sum(dp[-1]) % MOD)
