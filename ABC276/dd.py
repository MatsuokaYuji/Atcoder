import math

n = int(input())
A = list(map(int,input().split()))

dic={}
dic_={}

l = []

g = 0
for a in A:
    g = math.gcd(g, a)

ans = 0

for a in A:
    a /= g
    while a%2==0:
        a /= 2
        ans += 1
    
    while a%3==0:
        a /= 3
        ans += 1

    if a!=1:
        print(-1)
        exit()

print(ans)
        
    
