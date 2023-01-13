




N, K = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

tmp = max(A)

C = []
for i in range(N):
  if A[i] == tmp:
    C.append(i + 1)


for num in B:
  if num in C:
    print("Yes")
    exit()
print("No")
