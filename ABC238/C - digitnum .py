





N = int(input())
L = len(N)
MOD = 998244353

def g(x):
    return x * (x+1)//2
ans = 0
for i in range(1,L+1):
    if i !=L:
        k = (10**i-1) - (10**(i-1)-1)
    else:
        k = N - (10**(i-1) -1)
    ans += g(k)
    ans %= MOD
print(ans)