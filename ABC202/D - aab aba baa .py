



import math

A,B,K = map(int,input().split())

a = A
b = B
ans = ""

while a>0 and b>0:
    c = math.comb(a-1+b,a-1)
    if K<=c:
        ans+="a"
        a-=1
    else:
        ans+="b"
        b-=1
        K-=c
ans+="a"*a
ans+="b"*b
print(ans)


