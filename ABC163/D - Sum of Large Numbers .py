









N,K = map(int,input().split())

MOD = 10**9+7
ans = 0
for k in range(K,N+2):
    a = k*(k-1)/2
    b = k*(2*N-k+1)/2
    d = b-a+1
    ans+=(d%MOD)
print(int(ans%MOD))