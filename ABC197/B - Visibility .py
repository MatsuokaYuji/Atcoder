








H,W,X,Y = map(int,input().split())


S = [input() for _ in range(H)]

ans = 1
for j in range(Y-2,-1,-1):
    x = S[X-1][j]
    if x == "#":
        break
    else:
        ans+=1
for j in range(Y,W):
    x = S[X-1][j]
    if x == "#":
        break
    else:
        ans+=1
for i in range(X-2,-1,-1):
    x = S[i][Y-1]
    if x == "#":
        break
    else:
        ans+=1
for i in range(X,H):
    x = S[i][Y-1]
    if x == "#":
        break
    else:
        ans+=1
print(ans)
