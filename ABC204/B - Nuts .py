












N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    if A[i]<=10:
        continue
    else:
        tmp = A[i]-10
        ans+=tmp
print(ans)