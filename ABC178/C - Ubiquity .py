








N = int(input())
MOD = 10**9+7

a = 10**N%MOD
b = 9**N%MOD
c = 8**N%MOD


ans = a-2*b +c
print(ans%MOD)