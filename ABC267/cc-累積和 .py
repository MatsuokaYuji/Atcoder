n,m = map(int,input().split())
A = list(map(int,input().split()))
 
sigma=sum([(i+1)*a for i,a in enumerate(A[:m])]) #最初だけO(M)で計算
sumB = sum(A[:m]) #累積和
result =sigma
 
for i in range(n-m):
  sigma = sigma - sumB+ m*A[i+m]
  sumB = sumB - A[i] + A[i+m] #最もインデックスの小さい項を引き、次の項を足して更新
  if sigma>result:
    result = sigma
print(result)