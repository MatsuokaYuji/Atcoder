N = int(input())
A = list(map(int, input().split()))
print(A)

ans = 0

tmpMax = A[0] 
# i = 0 - N-1
# N =5 i= 0,1,2,3,4
# [2, 1, 5, 4, 3]
# 1>=2
for i in range(N):
    x = A[i]
    if x>=tmpMax:
        tmpMax = x
    else:
        d = tmpMax - x
        ans+=d

print(ans)

    
