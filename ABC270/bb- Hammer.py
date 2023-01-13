

X,Y,Z = map(int,input().split())

if X >0:
    if Y<0 or X<Y:
        print(X)
        exit()
    elif 0<Y<X:
        if 0<Z<Y:
            print(X)
            exit()
        elif Z<0:
            print(X+abs(Z)*2)
            exit()
        else:
            print(-1)
            exit()
else:
    if Y>0 or X>Y:
        print(abs(X))
        exit()
    elif X<Y<0:
        if 0>Z>Y:
            print(abs(X))
            exit()
        elif Z>0:
            print(abs(X)+abs(Z)*2)
            exit()
        else:
            print(-1)
            exit()