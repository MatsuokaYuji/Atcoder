





N = int(input())

a1 = 21


if N>=60:
    a1=22
    N-=60
if N<10:
    print(str(a1)+":"+"0"+str(N))
else:
    print(str(a1)+":"+str(N))
