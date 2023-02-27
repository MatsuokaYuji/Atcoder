




N = int(input())
S = input()

s = set()
s.add((0,0))
nowx = 0
nowy = 0
# print(dp)
for i in range(N):
  x = S[i]
  if x =="R":
    nowx+=1
    if (nowx,nowy) in s:
      print("Yes")
      exit()
    s.add((nowx,nowy))
  if x =="L":
    nowx-=1
    if (nowx,nowy) in s:
      print("Yes")
      exit()
    s.add((nowx,nowy))
  if x =="U":
    nowy+=1
    if (nowx,nowy) in s:
      print("Yes")
      exit()
    s.add((nowx,nowy))
  if x =="D":
    nowy-=1
    if (nowx,nowy) in s:
      print("Yes")
      exit()
    s.add((nowx,nowy))
print("No")



