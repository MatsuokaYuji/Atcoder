



# N,S = map(int,input().split())


# # i(0-100)枚目までめくって総和をj(0-10000)にできているか
# dp = [[False] * (S+1) for _ in range(N+1)]

# dp[0][0] = True

# k = []
# for i in range(N):
#     A,B = map(int,input().split())
#     k.append((A,B))

# for i in range(1,N+1):
#     a,b = k[i-1]
#     for j in range(S+1):
#         if dp[i-1][j] == True and a+j <=S:
#             dp[i][j+a] = True
#         if dp[i-1][j] == True and b+j <=S:
#             dp[i][j+b] = True
# if dp[-1][-1] == True:
#     print("Yes")
# else:
#     print("No")
#     exit()

# # 復元
# ans = []
# tmp = S

# for i in range(N,0,-1):
#     a,b = k[i-1]
#     if dp[i][tmp] == True:
#         if dp[i-1][tmp-a] == True:
#             ans.append("H")
#             tmp-=a
#         elif dp[i-1][tmp-b] == True:
#             ans.append("T")
#             tmp-=b
# print("".join(reversed(ans)))



N,S = map(int,input().split())

dp = [[""] * 10001 for i in range(N+1)]

for i in range(N):
    a,b = map(int,input().split())
    for j in range(10001):
        if i==0:
            dp[1][a] = "H"
            dp[1][b] = "T"
        else:
            if dp[i][j] != "":
                dp[i+1][j+a] =  dp[i][j] + "H"
                dp[i+1][j+b] =  dp[i][j] + "T"
if dp[N][S] == "":
    print("No")
else:
    print("Yes")
    print(dp[N][S])