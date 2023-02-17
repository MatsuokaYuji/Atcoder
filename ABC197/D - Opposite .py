









def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


# 三角関数、ベクトル
import math

N = int(input())
x0,y0 = map(int,input().split())
s,t = map(int,input().split())

center_x,center_y = (x0+s)/2,(y0+t)/2 

r = get_distance(x0,y0,center_x,center_y)
# print(r)
radCenterToP0 = math.atan2(y0-center_y,x0-center_x)

radDivN = 2 * math.pi/N

sum = radCenterToP0 + radDivN

x1 = center_x + r * math.cos(sum)
y1 = center_y + r * math.sin(sum)


# print(radCenterToP0)
# print(sum)
print(x1,y1)
