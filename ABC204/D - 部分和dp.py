






N = int(input())

T = [0] + list(map(int, input().split()))

S = sum(T)


dp = [[False]*(S+3) for i in range(N+3)]

dp[0][0] = True


for i in range(1,N+1):
    for j in range(S+1):
        if dp[i-1][j]:
            dp[i][j] = True
        if j-T[i] >=0 and dp[i-1][j-T[i]]:
            dp[i][j] = True
ans = 10**15
for i in range(S):
    if dp[N][i]:
        ans = min(ans,max(i,S-i))
print(ans)
