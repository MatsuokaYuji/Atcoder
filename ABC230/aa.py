











N = int(input())

s = "AGC0"

if N>=42:
    s+=str(N+1)
    print(s)
else:
    if N >=10:
        s+=str(N)
        print(s)
    else:
        s+= "0" + str(N)
        print(s)
