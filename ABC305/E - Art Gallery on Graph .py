

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

N,M,K = map(int,input().split())
uf = UnionFind(N+1)
for i in range(M):
    u,v = map(int,input().split())
    uf.unite(u,v)

K = int(input())
ng = set()
for i in range(K):
  x,y = map(int,input().split())
  s = uf.root(x)
  t = uf.root(y)
#   print(s,t)
  ng.add((min(s,t),max(s,t)))
# print(ng)

Q = int(input())
ans = []
for i in range(Q):
  p,q = map(int,input().split())
  p = uf.root(p)
  q = uf.root(q)
#   実際に辺を繋ぐのではなく、rootがngの集合に含まれているかどうかを見る
#   print(i,"a")
  if (min(p,q),max(p,q)) in ng:
    print("No")
  else:
    print("Yes")

