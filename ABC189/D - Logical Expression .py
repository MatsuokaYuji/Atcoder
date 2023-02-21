








N = int(input())
S = [input() for _ in range(N)]

# xをiまで決めてyがTrue or Falseであるような組み合わせ数
# 0 == False,1 = True
dp = [[0] * (2) for _ in range(N+1)]
dp[0][0] = 1
dp[0][1] = 1


for i in range(1,N+1):
    d = S[i-1]
    if d =="AND":
        dp[i][1] += dp[i-1][1]
        dp[i][0] += (2*dp[i-1][0]) + dp[i-1][1]
    else:
        dp[i][1] += (dp[i-1][1]*2)  + dp[i-1][0]
        dp[i][0] += dp[i-1][0]
print(dp[-1][1])


# N = int(input())
# T = 1
# F = 1
# for i in range(N):
#     exp = input()
#     if exp == "AND":
#         F = T + 2*F
#     else:
#         T = 2*T + F

# print(T)