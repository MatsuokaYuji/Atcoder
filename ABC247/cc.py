





N,Q = map(int,input().split())

A = list(range(N+1))

indx = list(range(N+1))


for i in range(Q):
    x = int(input())

    # xのインデックス番号を確認
    x_indx = indx[x]

    if x_indx == N:
        left_x = A[x_indx-1]
        # 入れ替え
        A[x_indx],A[x_indx-1] = A[x_indx-1],A[x_indx]

        indx[x] = x_indx -1
        indx[left_x] = N
    else:
        right_x = A[x_indx+1]
        # 入れ替え
        A[x_indx],A[x_indx+1]=A[x_indx+1],A[x_indx]
        indx[x] = x_indx + 1
        indx[right_x] = x_indx
# Aを出力
# 0番目は不要なので1番目~
# 「*」をつけると[]なしで出力できる
print(*A[1:])
