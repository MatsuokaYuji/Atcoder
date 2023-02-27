



MOD = 998244353


N = int(input())


L = []
for i in range(N):
    A,B = map(int,input().split())
    L.append((A,B))



# N枚目まで決めてそれが裏か表かで何通りか
dp = [[0] * 2 for i in range(N)]

dp[0][0] = 1
dp[0][1] = 1

for i in range(1,N):
    prea = L[i-1][0]
    preb = L[i-1][1]
    for j in range(2):
        now = L[i][j]
        # b = L[i][1]
        if prea != now:
            dp[i][j] += dp[i-1][0]
            
        if preb != now:
            dp[i][j] += dp[i-1][1]
        dp[i][j]%=MOD
        
# print(dp)
ans = sum(dp[N-1])
ans%=MOD
print(ans)


