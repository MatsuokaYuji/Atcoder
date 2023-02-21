





N,X = map(int,input().split())

sake = 0

# 不動小数点の誤差に注意
for i in range(N):
    v,p = map(int,input().split())
    now = v*p
    sake+=now
    if sake>X*100:
        print(i+1)
        exit()
print(-1)
