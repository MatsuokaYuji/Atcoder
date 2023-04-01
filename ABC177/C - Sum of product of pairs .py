



N = int(input())
A = list(map(int, input().split()))


s = sum(A)
MOD = 10**9+7
ans = 0
for i in range(N-1):
    x = A[i]
    s-=x
    tmp = x*s
    ans+=tmp
    ans%=MOD
print(ans)

