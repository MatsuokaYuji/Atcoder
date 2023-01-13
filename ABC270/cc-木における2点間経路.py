


# 入力の受け取り
N,X,Y = map(int,input().split())

from collections import deque

# 入力
edges = [ list(map(int, input().split())) for i in range(N-1) ]

# 隣接リストの作成
G = [ list() for i in range(N) ]
for a, b in edges:
	G[a-1].append(b-1)
	G[b-1].append(a-1)


# [[1, 2], [0], [0, 3, 4], [2], [2]]

Q = deque()
Q.append(X-1)

upper = [-1] * N
upper[X-1] = -2

# 幅優先探索
while len(Q) > 0:
    # キュー Q の先頭要素を取り除き、その値を now に代入する
    # 頂点now
    now = Q.popleft()
    # 頂点と隣接する点について調べる
    for nxt in G[now]:
        # 未確定ならそいつの頂点は今の頂点nowなのでupperに追加し、nxtをQに追加
        if upper[nxt] ==-1:
            upper[nxt] = now
            Q.append(nxt)
ans = []
now = Y - 1

while upper[now]!=-2:
    ans.append(now)
    now = upper[now]
ans.append(X-1)
for i in ans[::-1]:
    print(i+1,end =" ")



