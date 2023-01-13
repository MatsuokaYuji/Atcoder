

# 入力の受け取り
N=int(input())
A=list(map(int,input().split()))

# 出現回数の確認リスト
Count=[0]*(10**6)

# i=0~(N-1)
for i in range(N):
    # 出現回数をカウント
    Count[A[i]]+=1
 
# i=0~(10^6-2)
for i in range(10**6-1):
    # 一つ前の数を足していく
    Count[i+1]+=Count[i]

# 上記の処理でCount[x]=「Aにあるxより小さい要素の数」となる

# 答え
ans=0

# j=0~(N-1)
for j in range(N):
    # (Ajより小さい要素の数)*(Ajより大きい要素の数)
    ans+=Count[A[j]-1]*(N-Count[A[j]])

# 答えを出力
print(ans)



# 別解
# from collections import Counter
# def comb(n, r):
#     num = 1
#     den = 1
#     for i in range(r):
#         num *= (n - i)
#         den *= (r - i)
#     return num // den


# def main():
#     N = int(input())
#     A = list(map(int, input().split()))
#     C = Counter(A)
#     ans = comb(N, 3)
#     for c in C.values():
#         ans -= comb(c, 2) * (N - c)
#         ans -= comb(c, 3)
#     print(ans)


# if __name__ == '__main__':
#     main()