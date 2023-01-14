









N,K,X = map(int,input().split())
A = list(map(int, input().split()))

ans = sum(A)
import heapq
a = list(map(lambda x: x*(-1), A))

heapq.heapify(a)

while True:
    if K == 0:
        print(ans)
        exit()
    if ans<=0:
        ans = 0
        print(ans)
        exit()
    if len(a)==0:
        ans=0
        break
    d = heapq.heappop(a)*(-1)
    tmp = d-X
    if tmp<=0:
        K-=1
        ans-=d
    else:
        syou = d//X
        if K-syou<0:
            ans = ans - K*X
            print(ans)
            exit()
        K-=syou
        ans-=syou*X
        if d%X !=0:
            amari = d%X
            heapq.heappush(a,amari*(-1))
print(ans)

