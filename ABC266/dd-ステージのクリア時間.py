N = int(input())

Size = [[-1,0] for i in range(10**5+1)]

for i in range(N):
    T,X,A = map(int,input().split())
    Size[T] = [X,A]

dp = [[0,0,0,0,0] for i in range(10**5+1)]


for t in range(1,10**5+1):
    dp[t][0] = max(dp[t-1][0],dp[t-1][1])
    dp[t][1] = max(dp[t-1][0],dp[t-1][1],dp[t-1][2])
    dp[t][2] = max(dp[t-1][1],dp[t-1][2],dp[t-1][3])
    dp[t][3] = max(dp[t-1][2],dp[t-1][3],dp[t-1][4])
    dp[t][4] = max(dp[t-1][3],dp[t-1][4])

    X,A = Size[t]

    if X!=-1 and X<=t:
        dp[t][X] +=A
print(max(dp[10**5]))
