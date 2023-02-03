

# Union-Find 木
class unionfind:
	# n 頂点の Union-Find 木を作成
	# （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
	def __init__(self, n):
		self.n = n
		self.par = [ -1 ] * (n + 1) # 最初は親が無い
		self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1
	
	# 頂点 x の根を返す関数
	def root(self, x):
		# 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
		while self.par[x] != -1:
			x = self.par[x]
		return x
	
	# 要素 u, v を統合する関数
	def unite(self, u, v):
		rootu = self.root(u)
		rootv = self.root(v)
		if rootu != rootv:
			# u と v が異なるグループのときのみ処理を行う
			if self.size[rootu] < self.size[rootv]:
				self.par[rootu] = rootv
				self.size[rootv] += self.size[rootu]
			else:
				self.par[rootv] = rootu
				self.size[rootu] += self.size[rootv]
	
	#  要素 u と v が同一のグループかどうかを返す関数
	def same(self, u, v):
		return self.root(u) == self.root(v)

# https://qiita.com/Waaaa1471/items/fb2e1b0b3cd1a921054d#dmake-bipartite-2

N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]
	
# クエリの処理
uf = unionfind(2*N)

for a, b in edges:
    a-=1
    b-=1
    uf.unite(a,b+N)
    uf.unite(b,a+N)

for i in range(N):
    if uf.same(i,i+N):
        print(0)
        exit()

def com(n):
    return n * (n-1)//2
ans = com(N) - M 

# 各連結成分(色別)の個数を、親で管理
g = [0 for i in range(N)]
for i in range(N):
    g[uf.root(i)] +=1

for j in range(N):
    ans-=com(g[j])
print(ans)