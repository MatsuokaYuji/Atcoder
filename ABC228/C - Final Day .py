

from collections import defaultdict

d = defaultdict(int)


N,K = map(int,input().split())

# 三日目終了時の点数の合計、何位で、K位のやつと


for i in range(1,N+1):
    P = list(map(int, input().split()))
    p = sum(P)
    d[i] = p
# print(d)
dic = sorted(d.values(), reverse=True)
# print(dic2)
# defaultdict(<class 'int'>, {1: 440, 2: 624, 3: 126, 4: 466})
# [624, 466, 440, 126]

seek = dic[K-1]
for i in range(1,N+1):
    tmp = d[i]
    if seek-tmp >300:
        print("No")
    else:
        print("Yes")