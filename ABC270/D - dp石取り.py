





import sys
sys.setrecursionlimit(10**9)



# ゲーム
# 再帰
N,K = map(int,input().split())
A = list(map(int, input().split()))

dp = [None] * (N+1)
        
def dfs(x):
    if dp[x] !=None:
        return dp[x]
    ret = 0
    for i in range(K):
        if x>=A[i]:
            ret = max(ret,A[i] + (x-A[i])-dfs(x-A[i]))
    dp[x] = ret
    return ret
    
dfs(N)
print(dp[N])


# N,K=map(int,input().split())
# A=list(map(int,input().split()))
# dp=[0]*(N+1)
# dp[0]=0
# for i in range(1,N+1):
#     for j in range(K):
#         if i-A[j]<0:break
#         dp[i]=max(dp[i],A[j]+(i-A[j])-dp[i-A[j]])


# print(dp[-1])