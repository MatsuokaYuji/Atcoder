


N = int(input())


A = list(map(int, input().split()))

B = [0,0,0,0]
ans = 0


for i in range(N):
  B[0] = 1
  a = A[i]
  for j in range(3,-1,-1):
    if B[j] and j + a >= 4:
      ans+=1
    elif B[j]:
      B[j+a] = 1
    B[j] = 0
print(ans)

