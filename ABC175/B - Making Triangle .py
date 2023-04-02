









N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            a,b,c = A[i],A[j],A[k]
            if a+b>c and a+c>b and b+c>a and a!=b and b!=c and c!=a:
                ans+=1
print(ans)

