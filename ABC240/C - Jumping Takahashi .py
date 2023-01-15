










N,X = map(int,input().split())

A = [list(map(int, input().split())) for _ in range(N)]

dp = [[False] * (10001) for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
    a,b = A[i]
    for j in range(1,10001):
        if j-a<0:
            continue
        if j-b<0:
            dp[i+1][j] = dp[i][j-a]
            continue
        dp[i+1][j] = (dp[i][j-a] or dp[i][j-b])
        
print("Yes" if dp[N][X] else "No")