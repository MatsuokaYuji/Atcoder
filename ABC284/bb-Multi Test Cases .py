





T = int(input())

for i in range(T):
  ans = 0
  N = int(input())
  A = list(map(int, input().split()))
  for j in A:
    if j %2==1:
      ans+=1
  print(ans) 
  

  