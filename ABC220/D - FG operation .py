

MOD = 998244353

N = int(input())
A = list(map(int, input().split()))



# dp[i][j]: A のi要素目まで見て、一番左の要素がjである操作の方法が何通りあるか

dp = [[0] * 10 for i in range(N)]
dp[0][A[0]] = 1

for i in range(1,N):
    for j in range(10):
        f = (j+A[i]) %10
        g = (j*A[i]) %10
        dp[i][f] += dp[i-1][j]
        dp[i][g] += dp[i-1][j]
        dp[i][f]%=MOD
        dp[i][g]%=MOD

for i in range(10):
    print(dp[N-1][i])

    