
from collections import deque

Q = int(input())


que = deque()
for i in range(Q):
    S = input().split()
    q = int(S[0])
    if q == 1:
        x = int(S[1])
        c = int(S[2])
        que.append([x,c])
    if q == 2:
        c = int(S[1])
        ans = 0
        while 0<c:
            num,count = que.popleft()
            if count<=c:
                ans+= num*count
                c-=count
            else:
                ans+= num*c
                que.appendleft([num,count-c]) 
                c = 0


           
        print(ans)

