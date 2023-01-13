









L1,R1,L2,R2 = map(int,input().split())

Lmax = max(L1,L2)
Rmin = min(R1,R2)

ans = Rmin -Lmax

if ans <=0:
    print(0)
else:
    print(ans)