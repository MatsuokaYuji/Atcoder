








N,K = map(int,input().split())

for i in range(K):
    if N%200 == 0:
        N//=200
        continue
    N = int(str(N) + "200")
print(N)
    