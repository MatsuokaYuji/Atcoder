








N = int(input())

X = [None] * (N)
Y = [None] * (N)
Z = [None] * (N)

for i in range(N):
  X[i],Y[i],Z[i] = map(int,input().split())
INF = float('inf')
dp = [[INF] *N for i in range(2**N)]

#bitdp、桁dp
dp[0][0] = 0
# 動的計画法（dp[通った都市][今いる都市] となっている）
for i in range(2**N):
  for j in range(N):
    if dp[i][j] < INF:
      for k in range(N):
        if (i //(2**k))%2 ==0:
          dist = abs(X[k]-X[j]) + abs(Y[k]-Y[j]) + max(0,(Z[k] - Z[j]))
          dp[i +(2**k)][k] = min(dp[i+(2**k)][k],dp[i][j]+dist)
  
print(dp[-1][0])