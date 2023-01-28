


N = int(input())

MOD = 998244353
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CONST = 3001

# dp[i][c] i番目まで決めて最後がcの数列の数

dp = [[0] * CONST for i in range(N+1)]
dp[0][0] = 1
# dp[i+1][c] = sum(dp[i][:c+1]) % 998244353

for i in range(N):
    a = A[i]
    b = B[i]
    s = sum(dp[i][:a]) %MOD
    for c in range(a,b+1):
        s+=dp[i][c]
        s%=MOD
        dp[i+1][c] =s
# print(dp[N])
print(sum(dp[N]) % MOD)
