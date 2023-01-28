



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







# 隣接リスト作った時に、どれかの長さが3以上ならアウト
# mapで管理、登場するたびに+=1、どの頂点でも2超えたらアウト


def judge():
        
    # 隣接リストの作成
    N, M = map(int, input().split())
    #  クエリの処理
    uf = unionfind(N)

    C = [0] * N

    for i in range(M):
        a,b = map(int, input().split())
        a,b = a-1,b-1
        if uf.same(a,b):
            return False
        uf.unite(a,b)
        C[a] +=1
        C[b] +=1

    for i in range(N):
        if C[i]>=3:
            return False
    return True

print("Yes" if judge() else "No")