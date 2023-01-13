





N = int(input())

G = []

for i in range(N):
  A = input()
  A = list(A)
  
  G.append(A)


# 引数：(スタート行,スタート列,行方向,列方向)　
# →　マス目の数字を確認して値を返す
def Calc(s,R,GD,RD):
  result = ""
  for i in range(N):
    result += G[(s+GD*i)%N][(R+RD*i)%N]
  
  result = int(result)
  return result

ans = 0

for s in range(N):
  for t in range(N):
    ans = max(ans, Calc(s,t,-1,0))
    ans = max(ans, Calc(s,t,-1,1))
    ans = max(ans, Calc(s,t,0,1))
    ans = max(ans, Calc(s,t,1,1))
    ans = max(ans, Calc(s,t,1,0))
    ans = max(ans, Calc(s,t,1,-1))
    ans = max(ans, Calc(s,t,0,-1))
    ans = max(ans, Calc(s,t,-1,-1))
print(ans)