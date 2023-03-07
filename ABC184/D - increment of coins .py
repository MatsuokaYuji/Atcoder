




a,b,c = map(int,input().split())

# dp[a][b][c] := 袋の中の金貨、銀貨、銅貨の枚数がそれぞれ a,b,c であるときの、残り操作回数の期待値

m = 100
dp = [[[-1]*(m+1) for _ in range(m+1)] for _ in range(m+1)]

for i in range(a,m+1):
    for j in range(b,m+1):
        for k in range(c,m+1):
            if i==m or j==m or k ==m:
                dp[i][j][k] = 0

import sys
sys.setrecursionlimit(10 ** 6)  
def solve(a,b,c):
    if dp[a][b][c]>=0:
        ret = dp[a][b][c]
    else:
        ret = 0
        s = a+b+c
        ret+= a/s *(solve(a+1,b,c)+1)
        ret+= b/s *(solve(a,b+1,c)+1)
        ret+= c/s *(solve(a,b,c+1)+1)
        dp[a][b][c] = ret
    return ret

print(solve(a,b,c))