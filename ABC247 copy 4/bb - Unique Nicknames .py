




def judge():
  def judge2(u,idx):
    for i in range(N):
      if i==idx: continue
      if u in ST[i]:
        return False
    return True


  N = int(input())

  ST = [input().split() for i in range(N)] 

  for i in range(N):
    si,ti = ST[i]
    if not (judge2(si,i) or judge2(ti,i)):
      return False
  return True

print("Yes" if judge() else "No")
    


