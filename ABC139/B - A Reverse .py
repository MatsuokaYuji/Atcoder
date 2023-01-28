







A,B = map(int,input().split())

if B ==1:
    print(0)
    exit()

ans = 0
c = 0
for i in range(1,100):
    c = A*i - (i-1)
    if c>=B:
        print(i)
        exit()