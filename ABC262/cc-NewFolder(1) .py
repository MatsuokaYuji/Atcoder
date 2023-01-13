

N = int(input())


A = [0] + list(map(int, input().split()))
ans=0

k= 0

for i in range(1,N+1):
    if A[i] ==i:
        k+=1

ans+= k*(k-1)//2

for i in range(1,N+1):
    j = A[i]

    if i<j and A[j]==i:
        ans+=1
print(ans)
