

import math



A,B = map(int,input().split())

l = 2*B

x = math.pow(A/l, 2/3)

# print(x)

x = int(x) + 1
# print(x)
y = x + 1

a = A/math.sqrt(x) + (x-1) * B
b = A/math.sqrt(y) + (y-1) * B

print(min(a,b))