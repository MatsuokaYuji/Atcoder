A = list(map(int, input().split()))


mod = 998244353

a = A[0] % mod
b = A[1] % mod
c = A[2] % mod
d = A[3] % mod
e = A[4] % mod
f = A[5] % mod

ans = ((a * b * c) - (d*e*f)) % mod


print(ans)
