







N,M,X = map(int,input().split())

K = []


for i in range(N):
    k = list(map(int, input().split()))
    K.append(k)

from itertools import product, permutations,combinations
INF = float("INF")
ans = INF

for V in product(range(2), repeat=N):
    B = [0]*(M)
    # print(V)
    tmp = 0
    for i,v in enumerate(V):
        if v==1:
            C = K[i][0]
            tmp+=C
            f = K[i][1:]
            for m in range(len(f)):
                B[m]+=f[m]
    flag = False
    for i in B:
        if i<X:
            flag = True
    if flag:
        continue
    else:
        ans = min(ans,tmp)
        # print(ans)
        # print(V,B,tmp)
print(ans if ans!=INF else -1)

