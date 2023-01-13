





N = int(input())


S = list(map(int, input().split()))

A=[]

A.append(S[0])

for i in range(N-1):
  t = S[i+1] - sum(A)
  A.append(t)
print(*A)