def main():
  N = int(input())
 
  A = [list(map(int, input().split())) for _ in range(N)]
 
  # 選手i, j (i<j)の試合の番号をi*N+j+1として固有の番号をつけて、
  # それが条件を満たすべき順序関係を有向辺で表す
  # その結果、有向グラフが閉路をもつとき、条件を満たすような試合日程は存在しない
  # 存在しない場合は、最長パスが答え
  # 閉路検出とパス長の計算は、トポロジカルソートによって同時に行う
 
  G = collections.defaultdict(list)
  deg = collections.defaultdict(int)
  for i in range(1, N+1):
    Arow = A[i-1]
    for k in range(1, N-1):
      j_prev = Arow[k-1]
      j_next = Arow[k]
      prev_match = (min(i, j_prev), max(i, j_prev))
      next_match = (min(i, j_next), max(i, j_next))
      G[prev_match].append(next_match)
      deg[next_match] += 1
 
  # topological sort
  vx_deg0 = collections.deque()
  for k in G.keys():
      if deg[k]==0:
        vx_deg0.append((k, 1))
 
  ans = 0
  cnt = 0
  while vx_deg0:
      v_del, cost = vx_deg0.popleft()
      cnt += 1
      ans = max(ans, cost)
  
      for v_adj in G[v_del]:
          deg[v_adj] -= 1
          if deg[v_adj]==0:
              vx_deg0.append((v_adj, cost+1))


#同じ頂点数なら閉路なし
  if cnt==N*(N-1)//2:
    print(ans)
#頂点数が異なると閉路が存在している
  else:
    print(-1)
 
 
if __name__=="__main__":
  import sys
  input = sys.stdin.readline
  import collections
 
  main()
