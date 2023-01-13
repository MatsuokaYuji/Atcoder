












R,C = map(int,input().split())

a11,a12 = map(int,input().split())
a21,a22 = map(int,input().split())


if R + C ==2:
    print(a11)
if R + C ==4:
    print(a22)
if R + C == 3 and R ==1:
    print(a12)
if R + C == 3 and R ==2:
    print(a21)
