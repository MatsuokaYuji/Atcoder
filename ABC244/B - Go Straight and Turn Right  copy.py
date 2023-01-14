





N = int(input())

T = input()

x,y =(0,0)

d = ["E","S","W","N"]

count = 0
ahead = d[count]

for i in range(len(T)):
  if T[i] == "S":
    if ahead == "E":
      x+=1
    if ahead == "S":
      y-=1
    if ahead == "W":
      x-=1
    if ahead == "N":
      y+=1
  else:
    count+=1
    ahead = d[(count)%4]
print(x,y)

# 別解、アフィン変換
# N = int(input())
# T = input()
# x, y = 0, 0
# dx, dy = 1, 0
# for t in T:
#   if t == 'S': x, y = x + dx, y + dy
#   else: dx, dy = dy, -dx
# print(x, y)