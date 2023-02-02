







N,M= map(int,input().split())

X = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(int)

for i in range(M):
    c,y= map(int,input().split())
    d[c] = y

# N回コイントスをしてカウンタがKの時の最大値
# 紙に書いてトレースする
dp = [[0]*(N+1) for i in range(N+1)]

dp[0][0] = 0
for i in range(N):
    dp[0][i] = 0

for i in range(1,N+1):
    for k in range(N+1):
        if k==0:
            dp[i][k] = max(dp[i-1])
            continue
        if 1<=k<=i:
            dp[i][k] = dp[i-1][k-1] + X[i-1] + d[k]
print(max(dp[N]))
        

