





# 動的計画法(DP)を用います。
# dp[i][j] を、「 S の i 文字目までを使って、chokudai の j 文字目まで選択する方法」と定義します。
# ここで、N=∣S∣ , T=chokudai として、以下の漸化式が成り立ちます。



MOD = 10**9 +7
S = input()

f = ["c","h","o","k","u","d","a","i"]

dp = [[0] * 10 for i in range(len(S)+2)]
l = len(S)
for j in range(9):
    dp[0][j] = 0
for i in range(l):
    dp[i][0] = 1

for i in range(1,len(S)+1):
    for j in range(1,9):
        if S[i-1] == f[j-1]:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            dp[i][j]%=MOD
            
        else:
            dp[i][j] = dp[i-1][j]
            dp[i][j]%=MOD
        
print(dp[l][8])
