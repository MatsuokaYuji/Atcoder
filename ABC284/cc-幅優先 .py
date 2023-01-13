








from collections import deque

# 入力の受け取り
N,M = map(int,input().split())

from collections import deque

# 入力
edges = [ list(map(int, input().split())) for i in range(M) ]

# 隣接リストの作成
G = [ list() for i in range(N) ]
for a, b in edges:
	G[a-1].append(b-1)
	G[b-1].append(a-1)


# 訪問済み座標の管理
visited=[[False] for i in range(N+1)]

que=deque()
# 答え
ans=0
# 座標1から見ていく
Start= [i for i in range(N)]
for X in Start:
    que.append(X)
    if visited[X][0] == 0:
        ans+=1
    while len(que)>0:
        c = que.popleft()
        if visited[c][0]==0:
                # (4_1)訪問済みにする
                visited[c][0] = 1
                # (4_2)座標をキューに入れる
                for j in G[c]:
                    que.append(j)
        
print(ans)


