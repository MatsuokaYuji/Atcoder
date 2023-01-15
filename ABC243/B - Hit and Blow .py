N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

bset = set(B)
same = 0
diff = 0

for i in range(N):
  if A[i] not in bset:
    continue
  if A[i] == B[i]:
    same+=1
    continue
  diff+=1
  
print(same)
print(diff)
