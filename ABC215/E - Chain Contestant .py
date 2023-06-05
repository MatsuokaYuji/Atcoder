





# dp[i][S][list] i回目まで出場、出場したコンテスト状況がS、最後に出たのがlist

# bitdp
# 公式解説twitter 
# dp[i][S][j]=
# i番目のコンテストまでで、出たコンテストの種類の集合がSで、最後に出たコンテストの種類がj
# であるような、コンテストの出方の数

N = int(input())
S = input()
mod = 998244353
from collections import defaultdict
d = defaultdict(int)

alphabets  = "ABCDEFGHIJ"
for j in range(10):
    d[alphabets[j]] = j

set_num = 1<<10
# print(set_num)

dp = [[[0]*11 for i in range(set_num)] for i in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
    s = S[i]
    s_b = 1<<d[s]
    for j in range(set_num):
        for k in range(11):
            # コンテストに出ない
            dp[i+1][j][k] += dp[i][j][k]
            dp[i+1][j][k] %= mod
            
            # コンテストに出る
            # 最後に出たコンテストと一致なら
            if k == d[s] + 1:
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= mod
            # 最後に出たコンテストと一致しない
            else:
                # 同じ文字が連続ではないので、jがs_bを含むかどうか
                # jがs_bを含まない、つまりそのコンテストに出るのが初めてなら
                if s_b & j == 0: # 共通項がない、つまりそのコンテストに出るのが初めてなら
                    # i+1回目は和集合をとってjがs_bを含むように遷移する
                    dp[i+1][j|s_b][d[s]+1] += dp[i][j][k]
                    dp[i+1][j|s_b][d[s]+1] %= mod
ans = 0
for j in range(set_num):
    for k in range(11):
        if j != 0:
            ans += dp[N][j][k]
            ans %= mod
print(ans)



