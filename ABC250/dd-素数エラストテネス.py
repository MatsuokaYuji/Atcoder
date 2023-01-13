






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


N = int(input())

# N以下の素数リスト作成
primes = enum_primes(10 ** 6 + 5)


M = len(primes)

ans = 0
for i in range(M):
    t = primes[i] ** 3
    # primes[i]未満の素数を小さい順に全探索
    for j in range(i):
        if t * primes[j] > N:
            break
        ans +=1

print(ans)


