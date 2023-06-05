




N,K = map(int,input().split())

MOD = 998244353


S = [tuple(map(int,input().split())) for i in range(K)]
S.sort()
#dp累積
#dp高速化
# dp[i-v] のvは区間の累積和
dp = [0] * N
dp[0] = 1

dpsum = [0] * (N+1)
dpsum[1] = 1

for i in range(1,N):
    for l,r in S:
        li = i-r
        ri = i-l
        if ri <0:
            continue
        li = max(0,li)
        dp[i] += dpsum[ri+1] - dpsum[li]
        dp[i]%=MOD
    dpsum[i+1] = (dpsum[i] + dp[i]) %MOD
print(dp[-1])
# print(dpsum)
# print(dp)