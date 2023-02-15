

# # Union-Find 木
# class unionfind:
# 	# n 頂点の Union-Find 木を作成
# 	# （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
# 	def __init__(self, n):
# 		self.n = n
# 		self.par = [ -1 ] * (n + 1) # 最初は親が無い
# 		self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1
	
# 	# 頂点 x の根を返す関数
# 	def root(self, x):
# 		# 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
# 		while self.par[x] != -1:
# 			x = self.par[x]
# 		return x
	
# 	# 要素 u, v を統合する関数
# 	def unite(self, u, v):
# 		rootu = self.root(u)
# 		rootv = self.root(v)
# 		if rootu != rootv:
# 			# u と v が異なるグループのときのみ処理を行う
# 			if self.size[rootu] < self.size[rootv]:
# 				self.par[rootu] = rootv
# 				self.size[rootv] += self.size[rootu]
# 			else:
# 				self.par[rootv] = rootu
# 				self.size[rootu] += self.size[rootv]
	
# 	#  要素 u と v が同一のグループかどうかを返す関数
# 	def same(self, u, v):
# 		return self.root(u) == self.root(v)


# 別のuf、こっちの方がいいかも
class UnionFind:
    """
    0-indexed
    """

    from typing import List

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def unite(self, x, y) -> int:
        """
        xとyを併合
        """

        x = self.root(x)
        y = self.root(y)

        if x == y:
            return 0

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return self.parent[x]

    def is_same(self, x, y) -> bool:
        """
        xとyが同じ連結成分か判定
        """
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        """
        xの根を取得
        """
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        """
        xが属する連結成分のサイズを取得
        """
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """
        全連結成分のサイズのリストを取得
        計算量: O(N)
        """
        sizes = []

        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        """
        全連結成分のサイズの内容のリストを取得
        計算量: O(N・α(N))
        なんでACLはO(N)でできるんでしょうね
        """
        groups = dict()

        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)

        return list(groups.values())

N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]
uf = UnionFind(N+1)
ans = [0] * (N+1)
G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
    G[a].append(b)



count = 0
for i in range(N,0,-1):
    count+=1
    for j in G[i]:
        if not uf.is_same(i,j):
            uf.unite(i,j)
            count-=1
    ans[i-1] = count
    
for i in range(1,N+1):
    print(ans[i])
    