


N = int(input())

from collections import Counter

C = Counter()
for i in range(N):
    a,b = map(int,input().split())
    C[a]+=1
    C[a+b]-=1

days = sorted(C.keys())
# ans[i] i人ログインしている日数
ans= [0] *(N+1) 
prev_day = 0
cnt = 0
for curr_day in days:
    ans[cnt] += curr_day-prev_day
    cnt += C[curr_day]
    prev_day = curr_day
print(*ans[1:])

