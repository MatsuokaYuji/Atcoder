


N,X = map(int,input().split())
A = list(map(int, input().split()))

ans = 1
now = X-1
c = set()
c.add(X)

while True:
    x = A[now]
    if x not in c:
        ans +=1
        c.add(x)
        now = x-1
    else:
        print(ans)
        exit()