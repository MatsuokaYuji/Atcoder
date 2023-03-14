







from itertools import product, permutations,combinations



N,K = map(int,input().split())
T = []
for i in range(N):
    B = list(map(int, input().split()))
    T.append(B)



A = [i+1 for i in range(N-1)]

ans = 0
for i in permutations(A,N-1):
    tmp = 0
    x = i[0]
    y = i[-1]
    tmp += T[0][x]
    tmp+= T[y][0]
    for a in range(len(i)-1):
        pre = i[a]
        nex = i[a+1]
        tmp+= T[pre][nex]
    if tmp ==K:
        ans+=1


print(ans)