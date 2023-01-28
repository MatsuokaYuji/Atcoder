










h,w = map(int,input().split())

G = [input() for _ in range(h)]




dp = [[-1<<60] * (w+1) for _ in range(h+1)]

dp[1][1] = 1
for i in range(1,h+1):
  for j in range(1,w+1):

    if j-1>=1 and i-1>=1:
        if G[i-1][j-1] == ".":
            dp[i][j] = max(dp[i][j-1],dp[i-1][j]) + 1
    elif j-1>=1:
        if G[i-1][j-1] == ".":
            dp[i][j] = dp[i][j-1] + 1
    elif i-1>=1:
        if G[i-1][j-1] == ".":
            dp[i][j] = dp[i-1][j] + 1
    else:
        continue
ans = 0
for i in dp:
    ans = max(ans,*i)
print(ans)

# INF = 1 << 60


# def main():
#     H, W = map(int, input().split())
#     C = [list(input()) for _ in range(H)]
#     dp = [[-INF] * W for _ in range(H)]
#     dp[0][0] = 1
#     for row in range(H):
#         for col in range(W):
#             if row == col == 0:
#                 continue
#             if C[row][col] == ".":
#                 d1 = dp[row - 1][col] if row - 1 >= 0 else -INF
#                 d2 = dp[row][col - 1] if col - 1 >= 0 else -INF
#                 dp[row][col] = max(d1, d2) + 1
#     ans = 0
#     for dp_row in dp:
#         ans = max(ans, *dp_row)
#     print(ans)


# if __name__ == '__main__':
#     main()




