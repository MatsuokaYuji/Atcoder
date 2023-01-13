


N = int(input())


A = list(map(int, input().split()))

G = [0] * (2*N+ 1)
for i in range(1,N+1):
    G[2*i-1] = A[i-1]
    G[2*i] = A[i-1]

## [1, 3, 5, 2]
## [0, 1, 1, 3, 3, 5, 5, 2, 2]



# # 動的計画法（dp[x] は社員 x の部下の数）
# dp = [ 0 ] * (2 * N + 1)
# dp[1] = 0
# for i in range(N, 0, -1):
# 	for j in G[i]:
# 		dp[i] += (dp[j] + 1)

# # 答え (dp[1], dp[2], ..., dp[N]) を空白区切りで出力
# print(*dp[1:])


ans = [0] * (2*N+ 1)

for i in range(1,len(G)):
    if i %2 ==0:
        ans[i] = ans[i-1] 
    else:
        ans[i] = ans[G[i]-1] +1
    
    
for i in ans:
    
    print(i)




