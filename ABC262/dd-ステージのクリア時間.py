







N,X = map(int,input().split())


L = []

T=0

for i in range(N):
    A,B = map(int,input().split())
    T = T + A + B
    if i==0:
        t = T+B*(X-1)
        L.append(t)
    else:
        if (X-(i+1)) <=0:
            break
        t = T + B *(X-(i+1))
        L.append(t)

print(min(L))