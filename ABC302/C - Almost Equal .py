



N,M = map(int,input().split())
S = [list(input()) for _ in range(N)]
import itertools
a = list(itertools.permutations(S))


for i in range(len(a)):
    flag = True
    d = a[i][0]

    for j in range(N-1):
        count = 0
        e = a[i][j+1]
        for k in range(M):
            if d[k] != e[k]:
                count+=1
        if count !=1:
            flag = False
            break
        d = a[i][j+1]
    if flag :
        print("Yes")
        exit()
    

print("No")
    # print(a[i])
    # print(a[i][0])


