




from collections import deque


N = int(input())

A = [[0]]
T = [0]

for i in range(N):
    t,k,*a = map(int,input().split())
    T.append(t)
    if k>0:
        A.append(a)
    else:
        A.append([-1])


q = deque()
q.append(N)

learn = [False] * (N+1)
learn[N] = True

while q:
    waza = q.popleft()
    for i in A[waza]:
        if i==-1:
            break
        if learn[i] == False:
            q.append(i)
            learn[i] = True

ans=0

for i in range(1,N+1):
    if learn[i] == True:
        ans+= T[i]

print(ans)