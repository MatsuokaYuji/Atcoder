

N = int(input())


ans=10**15

# 「0」~「9」の表示秒数記録リスト
# 0：[0,1,2,3]⇔Time[0]=[0,1,2,3]　というように記録する
Time=[[] for i in range(10)]

# 各数の出現回数を数えるリスト
# C[1][2]=3なら「1」が2文字目に3回表示された　という意味
Count=[[0]*10 for i in range(10)]


for i in range(N):
    S = input()

    for x in range(10):
        # Sのx文字目を整数へ変換
        Sint=int(S[x])

        # 出現回数をプラス1
        Count[Sint][x]+=1
        # 表示秒数を記録
        # (出現回数-1)*10をプラスする
        Time[Sint].append(x+(Count[Sint][x]-1)*10)

for i in range(10):
    ans = min(ans,max(Time[i]))
print(ans)