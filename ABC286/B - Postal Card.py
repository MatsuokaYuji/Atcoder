












N,M = map(int,input().split())

S =[]
T = []

for i in range(N):
  s = input()
  s = s[3:]
  S.append(s)
for i in range(M):
  t = input()
  T.append(t)

ans = 0
for i in range(N):
  flag = True
  for j in range(M):
    if S[i] == T[j] and flag:
      ans+=1
      flag = False
print(ans)