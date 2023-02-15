




# N,K,D=[int(nkd) for nkd in input().split()]
# A=[int(a) for a in input().split()]
# dp=[[[-1 for _ in range(K+1)] for _ in range(N+1)] for _ in range(D)]
# # dp[0][0][0]=0
# # for n in range(N):
# #     for k in range(K+1):
# #         for d in range(D):
# #             if dp[d][n][k]>=0:
# #                 # 選ばない操作
# #                 dp[d][n+1][k]=max(dp[d][n][k],dp[d][n+1][k])

# #                 # 選ぶ操作
# #                 # 既に K個の総和になっている場所は更新しない
# #                 if k<K:
# #                     dp[(d+A[n])%D][n+1][k+1]=max(dp[d][n][k]+A[n],dp[(d+A[n])%D][n+1][k+1])

# # if dp[0][-1][-1]>=0:
# #     print(dp[0][-1][-1])
# # else:
# #     print(-1)

# A1~Aiまででx個の和を取った時、余りがdになるものの最大値
N,K,D = map(int,input().split())
A = [0] + list(map(int, input().split()))
dp = [[[-1]*D for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    dp[i][1][A[i]%D] = A[i]

for i in range(2,N+1):
    for x in range(1,min(i+1,K+1)):
        for d in range(D):
            dp[i][x][d] = max(dp[i][x][d],dp[i-1][x][d])
            if dp[i-1][x-1][d] !=-1:
                dp[i][x][(d+A[i])%D] = max(dp[i][x][(d+A[i])%D],dp[i-1][x-1][d]+ A[i])

print(dp[N][K][0])



