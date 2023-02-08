





N,K = map(int,input().split())

mat = []

for i in range(N):               
    a,b = map(int,input().split())
    mat.append((a,b))
mat.sort()

now = K

for i in range(N):
    a,b = mat[i]
    if now>=a:
        now+=b
    else:
        break
print(now)