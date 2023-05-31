



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

N, Q = map(int, input().split())
queries = [ list(map(int, input().split())) for i in range(Q) ]


# クエリの処理
uf = UnionFind(N)


for tp, u,v in queries:
    if tp == 1:
        uf.unite(u,v)
    if tp == 2:
        if uf.same(u,v):
            print("Yes")
        else:
            print("No")
