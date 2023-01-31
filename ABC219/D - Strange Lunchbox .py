

N = int(input())
X,Y = map(int,input().split())

INF = float('inf')
# dp[i][j][k]: i 番目の弁当まで使えるとき(j,k)にするのに必要な弁当の個数の最小値
dp = [[[INF] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0
P = []

for i in range(N):
    A,B = map(int,input().split())
    P.append((A,B))

for i in range(N):
    x,y = P[i]
    for j in range(X+1):
        js = min(x+j,X)
        for k in range(Y+1):
            ks = min(y+k,Y)
            dp[i+1][j][k] = min(dp[i+1][j][k],dp[i][j][k])
            dp[i+1][js][ks] = min(dp[i+1][js][ks],dp[i][j][k] + 1)
print(dp[N][X][Y] if dp[N][X][Y] < INF else -1)