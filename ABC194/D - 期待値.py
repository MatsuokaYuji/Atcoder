# 確率 p=0) で成功する試行を、
# 成功するまで行うときの試行回数(最後の成功した回も含む) 
# の期待値は 1/pである



N = int(input())
ans = 0

for i in range(1,N):
    ans+= N/(N-i)
print(ans)