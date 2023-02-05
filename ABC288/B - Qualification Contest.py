












N,K = map(int,input().split())

S = []
for i in range(N):
  s = input()
  S.append(s)

d = S[:K]
d.sort()

for i in d:
  print(i)
