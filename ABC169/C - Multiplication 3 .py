
import math

A,B = map(float,input().split())

A = int(A)
B = round(B*100)

ans = A*B
ans = ans//100

print(int(ans))