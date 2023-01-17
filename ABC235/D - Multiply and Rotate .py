










from collections import deque
from sre_constants import IN

a,N = map(int,input().split())

INF = 1<<62
max_N = 10**6 +1

# 幅優先探索の初期化（dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意）
dist = [INF] * max_N
dist[1] = 0
Q = deque((1,))

# 幅優先探索
while Q:
    x = Q.popleft()
    new_cost = dist[x] +1
    # 操作1
    d1 = x * a
    if d1<max_N:
        if new_cost <dist[d1] :
            dist[d1] = new_cost
            Q.append(d1)
    # 操作2
    if x>=10 and x %10!=0:
        d2 = int(str(x%10) + str(x//10))
        if new_cost <dist[d2] :
            dist[d2] = new_cost
            Q.append(d2)
if dist[N] != INF:
    print(dist[N])
else:
    print(-1)
	