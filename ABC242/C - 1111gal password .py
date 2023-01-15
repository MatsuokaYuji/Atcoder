


MOD = 998244353
N = int(input())


# Aの合計がK以下でかつ、Aのそれぞれの要素はM以下
dp = [ [ 0 ] * 11 for i in range(N+1) ]


# j = 0,10も含めるが0のまま
for i in range(1,10):
    dp[1][i] = 1

for i in range(1,N):
    for j in range(1,10):
        dp[i+1][j] += dp[i][j-1] + dp[i][j] + dp[i][j+1] 
        dp[i+1][j] %= MOD

ans = 0
for i in range(1,10):
    ans += dp[N][i]
    ans %=MOD
print(ans)

# PyPyで出さないとTLE
