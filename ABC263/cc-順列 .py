




import itertools

N,M = map(int,input().split())

a = []
for i in range(M):
    a.append(i+1)


for balls in itertools.permutations(a, N):
    flag = False
    start = balls[0]
    for i in balls:
        if start>i:
            flag = False
            break
        else:
            start = i
            flag = True
    if flag:
        print(*balls)

