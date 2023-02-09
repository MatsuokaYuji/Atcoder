


from collections import deque

N = int(input())

S = [deque() for _ in range(N)]

for i in range(N):
    t,l,r = map(int,input().split())
    if t==1:
        S[i].appendleft(l)
        S[i].append(r)
    if t==2:
        S[i].appendleft(l)
        S[i].append(r-0.5)
    if t==3:
        S[i].appendleft(l+0.5)
        S[i].append(r)
    if t==4:
        S[i].appendleft(l+0.5)
        S[i].append(r-0.5)

ans = 0

for i in range(N-1):
    for j in range(i+1,N):
        d1 = S[i][-1]
        d2 = S[i][0]
        e1 = S[j][-1]
        e2 = S[j][0]
        # if d1 < e2 or e1 < d2:
        #     continue
        # ans+=1
        # 2 つの閉区間 [a,b],[c,d] が共通部分を持つかの判定は
        #  max(a,c)≤min(b,d) ともかける
        ans+= (max(d2,e2)<=min(d1,e1))
print(ans)
