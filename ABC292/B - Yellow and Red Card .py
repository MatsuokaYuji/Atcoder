







from collections import defaultdict

d = defaultdict(int)


N,Q = map(int,input().split())


for i in range(Q):
    c,x = map(int,input().split())
    if c ==1:
        d[x]+=1
    if c ==2:
        d[x]+=2
    if c ==3:
        if d[x]>=2:
            print("Yes")
        else:
            print("No")