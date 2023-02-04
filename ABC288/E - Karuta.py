





N = int(input())

def LCS(S, T):
    # 初期化
    dp = [[0 for i in range(len(T) + 1)] for j in range(len(S) + 1)]

    # DP
    for i in range(len(S)):
        for j in range(len(T)):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
            if S[:i+1] == T[:j+1]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
    return dp[len(S)][len(T)]


P =[]
for i in range(N):
    s = input()
    P.append((s,i))
P.sort()

from collections import defaultdict
K = []
for i in range(N):
    ans = 0
    for j in range(i-1,N,2):        
        # print(P[i],P[j])
        d = LCS(P[i][0],P[j][0])
        ans = max(ans,d)
    K.append(ans)
# P[('a', 10), ('abra', 7), ('abracadabra', 0), ('acadabra', 3), ('adabra', 5), ('bra', 8), ('bracadabra', 1), ('cadabra', 4), ('dabra', 6), ('ra', 9), ('racadabra', 2)]

for i,a in P:
    print(K[a])
