








N = int(input())
A = list(map(int, input().split()))

ans = []

bef = A[0]
ans.append(bef)
for i in range(1,N):
    nex = A[i]
    t = nex-bef
    if t>=1:
        start = bef+1
        end = nex
        for j in range(start,end):
            ans.append(j)
    if t<=-1:
        start = bef-1
        end = nex
        for j in range(start,end,-1):
            ans.append(j)
    ans.append(nex)
    bef = nex
print(*ans)
        
    