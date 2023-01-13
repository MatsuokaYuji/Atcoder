



N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 隣接リストの作成
G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
	G[a].append(b)                      # 頂点 a に隣接する頂点として b を追加
	G[b].append(a)                      # 頂点 b に隣接する頂点として a を追加



# [[], [5, 4], [3, 5], [2, 5], [5, 1], [1, 4, 3, 2]]
ans= 0

for i in G:
    if len(i)<=1:
        continue
    for a in range (len(i)):
        for b in range(a+1,len(i)):
            if i[a] in G[i[b]]:
                ans+=1
print(ans//3)


# # 入力の受け取り
# N,M=map(int,input().split())

# # つながっている頂点を記録する二次元配列
# # 最初は全ての初期値をFalseにする
# connect=[[False]*(N+1) for i in range(N+1)]

# # M回
# for i in range(M):
#     # 入力の受け取り
#     U,V=map(int,input().split())
#     # 頂点Uと頂点Vがつながっている⇔Trueと記録
#     connect[U][V]=True
#     connect[V][U]=True

# # 答え
# ans=0

# # a=1~N
# for a in range(1,N+1):
#     # b=(a+1)~N
#     for b in range(a+1,N+1):
#         # c=(b+1)~N
#         for c in range(b+1,N+1):
#             # a,b,cが全てつながっていれば
#             if connect[a][b]==True and connect[b][c]==True and connect[c][a]==True:
#                 # 答えにプラス1
#                 ans+=1

# # 答えの出力
# print(ans)