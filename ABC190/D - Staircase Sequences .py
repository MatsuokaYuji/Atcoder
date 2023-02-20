


# 約数全列挙O(sqrt(N))
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]



N = int(input())

ans = 0
k = make_divisors(2*N)
# print(k)
for n in k:
    m = 2*N//n
    if m %2 != n%2:
        ans+=1
print(ans)
