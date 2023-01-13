

















N,K,Q = map(int,input().split())
A = list(map(int, input().split()))

L = list(map(int, input().split()))

B = [0] * 200

right = N
for i in A:
  B[i-1] =1

for i in L:
  #num-1は何番目かを表す
  num = A[i-1]
  if num == right:
    continue
  if B[num] == 1:
    continue
  if B[num] == 0:
    B[num] = 1
    B[num-1] = 0
    A[i-1]+=1


for i in range (len(B)-1):
  if B[i] ==1:
    print(i+1,end=" ")
if B[-1]==1:
  print(200)