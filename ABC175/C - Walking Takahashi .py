







from itertools import product, permutations,combinations



X,K,D = map(int,input().split())

X = abs(X)

k= X//D
r = X%D

if X-K*D>0:
    print(X-K*D)
    exit()

nokori = K-k

if nokori%2==0:
    ans = X-D*k
    print(ans)
else:
    ans = abs(X-D*(k+1))
    print(ans)