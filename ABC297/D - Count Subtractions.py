









A,B = map(int,input().split())

if A==B:
    print(0)
    exit()


a = min(A,B)
b = max(A,B)
ans = 0
s = set()
s.add(a)
s.add(b)
while True:
    r = b//a
    c = b%a
    s.add(b-a*r)
    if c==0:
        if b//a==2:
            ans+=1
            print(ans)
            exit()
        else:
                
            ans+=(r-1)
            print(ans)
            exit()
    else:
        ans+=(r)
        # print(ans)
        b = a
        a = min(s)
        
        # print(a,b)
        

