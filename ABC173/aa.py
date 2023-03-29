






import math
A,B = map(float,input().split())

# a = math.sqrt(A)
# b = B*100

# x = a*b
# x = x/100
# x = x*a

# print(int(x))
A = int(A)
B = round(100*B)
# B = 100*B
ans = A*B
ans = ans//100

# print(A,B)
# print(int(A*B))
print(int(ans))
