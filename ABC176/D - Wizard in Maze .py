import sys
sys.setrecursionlimit(500000)
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def TI(): return tuple(map(int,sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip())
#for i, pi in enumerate(p):
from collections import defaultdict,deque
import bisect
import itertools
dic = defaultdict(int)
dd = deque()
YN = ['No','Yes']

# 頂点数を V,辺数を Eとします。よく使われる実装ではこのようになります。
# ダイクストラ法（優先度付きキュー利用）：O(V+ElogV)
# 幅優先探索（キュー使用）：O(V+E)
# 01-BFS（両端キュー使用）：O(V+E)


# 01-bfs
# BFS+ダイクストラ
H,W = MI()
Cx,Cy = map(int,input().split())
Dx,Dy = map(int,input().split())

S = [input() for _ in range(H)]
INF = 10 ** 18

seen = [[INF] * W for _ in range(H)]

q = deque([(Cx-1,Cy-1,0)])
while q:
    # cntはワープした回数(パンチ)
    i, j, cnt = q.popleft()
    if seen[i][j] <cnt:
        continue
    # ワープしない場合
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < H and 0 <= nj < W and seen[ni][nj] > cnt and S[ni][nj] == ".":
                seen[ni][nj] = cnt
                
                # 0の辺を用いた場合は両端キューの先頭に加える。
                q.appendleft((ni, nj, cnt))
                # print(i,j,cnt,"not")
    # ワープする場合
    for di in range(-2,3):
        for dj in range(-2,3):
            if abs(di) + abs(dj) > 4:
                continue
            ni = i + di
            nj = j + dj
            if 0 <= ni < H and 0 <= nj < W and seen[ni][nj] > cnt + 1 and S[ni][nj] == ".":
                seen[ni][nj] = cnt + 1
                # 1の辺を用いた場合は両端キューの末尾に加える。
                q.append((ni, nj, cnt+1))
                # print(i,j,cnt+1,"yes")
# print(seen)
if seen[Dx-1][Dy-1] == INF:
    print(-1)
    exit()
print(seen[Dx-1][Dy-1])
# print(seen)





