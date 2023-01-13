N=int(input())

one=[]

# Nを2進数で表した際、1になる桁を格納
for i in range(60):
  if N>>i&1:
    one.append(i)

l=len(one)
# [0, 1, 3] oneの中身、この場合極論[0,1],[0,2][0,8]の全ての組み合わせの合計を見てる

# 1<<lで　2**len(one),8通りつまり0-7まで
for i in range(1<<l):
  now=0
#   0-2
  for j in range(l):
    # iをjbit右シフトして1かどうか判定
    if i>>j&1:
      now+=(1<<one[j])
  print(now)