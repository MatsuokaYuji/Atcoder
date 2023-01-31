







h,w,n = map(int,input().split())

R = []
C = []

for i in range(n):
    a,b = map(int,input().split())
    R.append(a)
    C.append(b)

Rs = sorted(set(R))
Cs = sorted(set(C))

Rd = {x:i for i,x in enumerate(Rs,1)}
Cd = {x:i for i,x in enumerate(Cs,1)}
# print(Rd)
# print(Cd)
Rf = {Rs[i]: i for i in range(len(Rs))}

for a,b in zip(R,C):
    print(Rd[a],Cd[b])
