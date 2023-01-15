



















N = int(input())

S = input()


for i in range(1,N):
  ans = 0
  for j in range(N-1):
    # print(i,j)
    if i+j>=N:
      continue
    if S[j] != S[j+i]:
      ans+=1
    else:
      break
    
  print(ans)
  


