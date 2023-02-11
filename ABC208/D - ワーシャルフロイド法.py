

# ワーシャルフロイド法
# ワーシャルフロイド法は重み付き有向グラフの全ペアの最短経路問題を、
# 頂点の数をNとしてO(N^3)で解くアルゴリズム
N, M = map(int, input().split())

inf = 10**10

time = [[inf] * (N+1) for inf in range(N+1)]

for i in range(1,N+1):
    time[i][i] = 0

for i in range(M):
    A,B,C = map(int,input().split())
    time[A][B] = C

ans = 0

for k in range(1,N+1):
    new_time = [[0] * (N+1) for _ in range(N+1)]
    for start in range(1,N+1):
        for goal in range(1,N+1):
            new_time[start][goal] = min(time[start][goal],time[start][k] + time[k][goal])
            if new_time[start][goal] !=inf:
                ans+= new_time[start][goal]
    time = new_time
print(ans)
