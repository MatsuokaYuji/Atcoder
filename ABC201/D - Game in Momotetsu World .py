




def translate(x):
    if x == "+":
        return 1
    else:
        return -1





H,W = map(int,input().split())


A = [list(map(translate, input())) for _ in range(H)]

INF = 10**18
# dp[i][j]は(i,j)のマスから最適な操作をしたときに
# 取り得る両者の差の最大値(青木くんの手番のマスでは最小値)
dp = [[-INF] * (W) for i in range(H)]
dp[-1][-1] = 0

for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        # A[y][x]<dp[y][x]であれば、dp=A-dpするたびにdpの正負が逆転する
        # そのため、全てmax判定でもおｋ
        if i < H-1:
            dp[i][j] = max(dp[i][j],A[i+1][j]-dp[i+1][j])
        if j < W-1:
            dp[i][j] = max(dp[i][j],A[i][j+1]-dp[i][j+1])

ans = dp[0][0]

if ans>0:
    print("Takahashi")
elif ans == 0:
    print("Draw")
else:
    print("Aoki")
