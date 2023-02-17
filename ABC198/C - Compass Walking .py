






import math

# 2点間の距離
def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

R,X,Y = map(int,input().split())

ans = 0
first_distance = get_distance(0,0,X,Y)
dis = first_distance
# print(dis)
while True:
    if dis == R:
        ans+=1
        print(ans)
        exit()
    if dis <= 2*R:
        ans+=2
        print(ans)
        exit()
    else:
        dis-=R
        ans+=1

