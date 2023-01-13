





N, A, B = map(int, input().split())
 
for i in range(A*N):
  a = []
  for j in range(B*N):
    if ((i//A) + (j//B)) % 2 == 0:
      a.append(".")
    else:
      a.append("#")
  print("".join(a))