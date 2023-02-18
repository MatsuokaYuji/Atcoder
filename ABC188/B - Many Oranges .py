





A,B,W = map(int,input().split())

W = W*10**3

tmpmin = float('INF')
tmpmax= -1

for n in range(1,10**6+1):
    l = A*n
    r = B*n
    if l <= W <= r:
        tmpmin = min(tmpmin,n)
        tmpmax = max(tmpmax,n)


if tmpmax == -1:
    print("UNSATISFIABLE")
else:
    print(tmpmin,tmpmax)