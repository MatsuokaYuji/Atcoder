



H, W = map(int, input().split())

S = [input() for _ in range(H)]

p = []

for i in range(H):
  for j in range(W):
    if S[i][j] == "o":
      p.append((i,j))

ar,ac = p[0]
br,bc = p[1]

ans = abs(ar-br) + abs(ac-bc)
print(ans)
