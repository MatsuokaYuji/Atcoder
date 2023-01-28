







N,X = map(int,input().split())

ans = [1]

for i in range(N):
    L,*A = map(int,input().split())
    # print(A)
    # print(*A)
    ans = [x * y for x in ans for y in A if x*y<=X]
print(ans.count(X))


