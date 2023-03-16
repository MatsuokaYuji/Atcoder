








import math

N = int(input())
A = list(map(int, input().split()))

x = 0
y = 0
z = 0
for i in A:
    d = abs(i)
    x+=d
    d2 = i**2
    y+=d2
    z = max(z,d)
print(x)
print(math.sqrt(y))
print(z)





