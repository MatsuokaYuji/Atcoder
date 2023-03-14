







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

A = list(map(int, input().split()))

A.sort()
m = A[-1]
cnt = [0] *(m+1)

for a in A:
    S = make_divisors(a)
    # print(S)
    for s in S:
        cnt[s]+=1
tmp = 0
ans = 0
# print(cnt)
for i,a in enumerate(cnt):
    if i == 1:
        continue
    if a>=tmp:
        tmp = a
        ans = i 


print(ans)



