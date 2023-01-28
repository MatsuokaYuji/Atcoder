








A,B = map(int,input().split())

a = str(A)
b = str(B)

la = len(a)
lb = len(b)

x = [True if la-lb>=0 else False]

if la == lb == 1:
    if A+B>=10:
        print("Hard")
        exit()


if x:
    for i in range(1,lb):
        c = int(a[-i])
        d = int(b[-i])
        if c+d >=10:
            print("Hard")
            exit()
else:
    for i in range(1,la):
        c = int(a[-i])
        d = int(b[-i])
        if c+d >=10:
            print("Hard")
            exit()
print("Easy")
