















A,B,C,D = map(int,input().split())


# エラストテネスのふるい
def enum_primes(n):
    prime_flag = [1] * (n + 1)
    prime_flag[0] = 0
    prime_flag[1] = 0

    i = 2
    while i * i <= n:
        if prime_flag[i]:
            for j in range(2 * i, n + 1, i):
                prime_flag[j] = 0
        i += 1
    return [i for i in range(n + 1) if prime_flag[i]]


# N以下の素数リスト作成
primes = enum_primes(201)


for x in range(A,B+1):
    ans=0
    for y in range(C,D+1):
        if x+y in primes:
            ans+=1
            continue
    if ans==0 and y==D:
        print("Takahashi")
        exit()
print("Aoki")