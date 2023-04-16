










import math
A, B, H, M = map(int, input().split())
theta1 = 2 * math.pi * (60 * H + M) / (12 * 60)
theta2 = 2 * math.pi * M / 60
x, y = A * math.cos(theta1), A * math.sin(theta1)
u, v = B * math.cos(theta2), B * math.sin(theta2)
d = math.sqrt((x - u) ** 2 + (y - v) ** 2)
print(d)