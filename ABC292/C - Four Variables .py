











# AB=X を満たす正整数 A,B の個数は X の正の約数の個数に等しいです。

N = int(input())

c = [0]*(N+1)
for a in range(1,N+1):
    for b in range(1,N+1):
        if a * b > N:
            break
        c[a*b]+=1
ans = 0
# print(c)
for i in range(N+1):
    ans+= c[i] * c[N-i]
print(ans)
