





# 重複ありの組み合わせ
# 重複組合せ

N,M,Q = map(int,input().split())

ans = 0
from itertools import combinations_with_replacement as comb_rplc
q = []
for i in range(Q):
    a,b,c,d= map(int,input().split())
    q.append((a,b,c,d))



for seq in comb_rplc(range(1, M+1), N):
    tmp = 0
    # print(seq)
    for i in range(Q):
        x = q[i]
        a,b,c,d = x
        # print(a,b,c,d)
        if seq[b-1]-seq[a-1] == c:
            tmp+=d
    ans = max(ans,tmp)
print(ans)
    



# dfsパターン
def dfs(seq):
    # 返り値は、すべての数列の得点の最大値 ans です。
    ans = 0
    if len(seq) == n:
        # 数列が完成したので、得点を計算します
        score_ret = 0
        for a, b, c, d in req:
            if seq[b-1] - seq[a-1] == c:
                score_ret += d
        return score_ret  # この数列の得点を返します
    else:
        # まだ数列が完成していません
        for i in range(seq[-1], m + 1):
            seq_next = seq + (i,)  # 長さ1のタプル(i,)を連結します
            score = dfs(seq_next)  # seq_nextから派生するすベての数列の中での、得点の最大値が返ってきます
            ans = max(ans, score)  # 最大の得点を更新します

    # 得点の最大値を返します
    return ans


n, m, q = list(map(int, input().split()))
# reqは[[a1,b1,c1,d1],[a2,b2,c2,d2]……]が入ったリストのリストです
req = [list(map(int, input().split())) for _ in range(q)]

# 最終的に答えが返ってくるようにします。処理はすべてdfsメソッドでやってもらいます。
# リストだとどこかで間違えて値を書き換えそうで怖いので、タプルにしておきます
# 1番目が1の場合以外は考えなくていいので、(1,)だけやります
ans = 0
score = dfs((1,))
ans = max(ans, score)
print(ans)










# ABC029-C
N = int(input())
import itertools

all = itertools.product('abc', repeat=N)
for x in all:
    print("".join(x))
