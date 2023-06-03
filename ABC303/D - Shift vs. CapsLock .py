

X,Y,Z = map(int,input().split())

S = input()

N = len(S)

f = float('inf')
dp = [[f for _ in range(2)] for _ in range(N+1)]

dp[0][0] = 0
dp[0][1] = Z

for i in range(N):
    dp[i][0] = min (dp[i][0],dp[i][1] + Z)
    dp[i][1] = min (dp[i][1],dp[i][0] + Z)

    if S[i] =="a":
        dp[i+1][0] = min(dp[i+1][0],dp[i][0]+X)
        dp[i+1][1] = min(dp[i+1][1],dp[i][1]+Y)

    else:
        dp[i+1][0] = min(dp[i+1][0],dp[i][0]+Y)
        dp[i+1][1] = min(dp[i+1][1],dp[i][1]+X)
print(dp[-1])
print(min(dp[-1]))