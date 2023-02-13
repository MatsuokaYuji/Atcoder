







H,W,C = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(H)]


# 方針、まず絶対値を考えやすくするため左下、右下と、反転verの2パターンに分ける
# 1点を固定(全探索)し、A[y2][x2] - C*(y2+x2)を最小化したい
# dpと累積和を使う

INF = int(1e18)

ans = INF

for _ in range(2):
    dp = [[INF] * (W) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i > 0:
                dp[i][j] = min(dp[i][j],dp[i-1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j],dp[i][j-1])
            ans = min(ans,A[i][j] * C(i+j) + dp[i][j])
            dp[i][j] = min(dp[i][j],A[i][j] - C * (i+j))
    print(A)
    A.reverse()
print(ans)