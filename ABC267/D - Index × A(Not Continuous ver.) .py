







N,M = map(int,input().split())

A = list(map(int, input().split()))

dp = [[None]*N for i in range(M)]

dp[0][0] = A[0]

for i,a in enumerate(A[1:-M+1]):
    dp[0][i+1] = max(a,dp[0][i])

for m in range(1,M):
    for n in range(m,N-M+m+1):
        if dp[m][n-1] == None:
            dp[m][n] = dp[m-1][n-1] + (m+1) * A[n]
            continue
        else:
            dp[m][n] = max(dp[m][n-1],dp[m-1][n-1] + (m+1) * A[n])
print(dp[-1][-1])

