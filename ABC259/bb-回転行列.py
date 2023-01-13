a, b, d = map(int, input().split()) # input

import math

d_rad = math.radians(d) # 角度法を弧度法に変換

a_rotated = a * math.cos(d_rad) - b * math.sin(d_rad)
b_rotated = a * math.sin(d_rad) + b * math.cos(d_rad)

print(a_rotated, b_rotated)