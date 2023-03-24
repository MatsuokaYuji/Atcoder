






# AB=X を満たす正整数 A,B の個数は X の正の約数の個数に等しいです。

N = int(input())

ans = 0
for a in range(1,N):
    b = (N-1)//a
    ans+=b
print(ans)


# N=int(input())

# # 約数の個数のテーブルを O(N logN) で作る
# div = [0] * (N+1)
# for d in range(1, N+1):
#   for n in range(d, N, d):
#     div[n] += 1

# ans = sum(div[:N])
# print(ans)