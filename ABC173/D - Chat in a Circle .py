









N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = 0
ans+=A[0]
tmp = 0
for i in range(1,N-1):
    if i%2==1:
        tmp+=1
    ans+=A[tmp]
print(ans)
    
    