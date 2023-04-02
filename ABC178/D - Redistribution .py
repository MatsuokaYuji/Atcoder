






MOD = 10**9+7
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# 長さk、すべての項が0以上の整数で総和がS-3*k
# S-3*k>=0よりkは1から[S/3]
S = int(input())
ans = 0
m = S//3

for k in range(1,m+1):
    a = S-3*k + (k-1)
    tmp = comb(a,k-1)
    ans+=tmp
    ans%=MOD
print(ans)