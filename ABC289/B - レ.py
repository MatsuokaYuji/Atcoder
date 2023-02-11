



N,M = map(int,input().split())
A = list(map(int, input().split()))
G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a in A:
	G[a].append(a+1)                      # 頂点 a に隣接する頂点として b を追加
	G[a+1].append(a)
from collections import deque


s =set()
ans = []
Q = deque()

for i in range(1,N+1):
    if i in s:
        continue
    Q.append(i)
    tmp = []
    tmp.append(i)
    s.add(i)
    g =G[i-1]
    # 幅優先探索
    while len(Q) > 0:       
    # キュー Q の先頭要素を取り除き、その値を pos に代入する
        pos = Q.popleft()
        for nex in G[pos]:
            if nex not in s:
                Q.append(nex)
                s.add(nex)
                tmp.append(nex)
    tmp = tmp[::-1]
    for j in tmp:
        ans.append(j)
print(*ans)

