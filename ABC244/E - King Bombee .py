
MOD = 998244353

N,M,K,S,T,X = map(int,input().split())


edges = [ list(map(int, input().split())) for i in range(M) ]

G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
	G[a].append(b)                      # 頂点 a に隣接する頂点として b を追加
	G[b].append(a) 
# dp、現在の移動回数、現在いる頂点、とおたxの回数が偶数かどうか

# dp0[K][T]が答え
dp0 = [[0] * (N+1) for _ in range(K+1)]
dp1 = [[0] * (N+1) for _ in range(K+1)]

dp0[0][S] = 1

for i in range(K):
  for u in range(1,N+1):
    for v in G[u]:
      if v==X:
        dp0[i+1][v] += dp1[i][u]
        dp1[i+1][v] += dp0[i][u]
      else:
        dp0[i+1][v] += dp0[i][u]
        dp1[i+1][v] += dp1[i][u]
      dp0[i+1][v] %=MOD
      dp1[i+1][v] %=MOD
print(dp0[K][T])
