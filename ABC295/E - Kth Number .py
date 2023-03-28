













L,N1,N2 = map(int,input().split())
A = []
B = []


for i in range(N1):
    v,l = map(int,input().split())
    A.append((v,l))

for i in range(N2):
    v,l = map(int,input().split())
    B.append((v,l))

ans,i,j,p,q = 0,0,0,0,0

while i<N1 and j<N2:
    a = A[i][0]
    c = A[i][1]
    b = B[i][0]
    d = B[i][1]
    if a == b:
        ans+= min(p+c,q+d) - max(p,q)
    if c<d:
        i+=1
        p+=c
    else:
        j+=1
        q+=d
print(ans)