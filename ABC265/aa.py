






x,y,n = map(int,input().split())

if 3*x -y >=0:
    a = n//3
    b = n%3
    print(y * a + x *b)
else:
    print(n*x)
