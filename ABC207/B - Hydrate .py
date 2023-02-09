


A,B,C,D = map(int,input().split())

ans = 0
count = A
x = C*D-B
if x<=0:
    print(-1)
    exit()



y1 = A/x
y2 = int(y1) 
if y1==y2:
    print(int(y1))
else:
    print(y2+1)




