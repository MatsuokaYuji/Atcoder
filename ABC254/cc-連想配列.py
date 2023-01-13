# 入力の受け取り
N,K=map(int,input().split())
a=list(map(int,input().split()))

# ソート後のA
aSorted=sorted(a)

# defaultdictをインポート
from collections import defaultdict

# a[i],a[i+K],a[i+2K],...に出てくる数字をカウントする連想配列
Count=defaultdict(int)

# i=0~(K-1)
for i in range(K):

    x=0
    # インデックスの範囲内である限り
    while i+K*x<N:
        # a[i+K*x]の個数をカウント
        Count[a[i+K*x]]+=1
        # 次のxへ
        x+=1
  
    x=0
    # インデックスの範囲内である限り
    while i+K*x<N:
        # ソート後のaについてaSorted[i+K*x]の個数をマイナス
        Count[aSorted[i+K*x]]-=1
        # もし個数がマイナスになったら
        if Count[aSorted[i+K*x]]<0:
            # ソート前とソート後で個数が違う
            # ⇔「No」を出力
            print("No")
            # 終了
            exit()
        
        # 次のxへ
        x+=1

# 「Yes」を出力
print("Yes")