

import math
A,B = map(int,input().split())

d = math.degrees(math.atan2(B,A))


a = math.cos(math.radians(d))
b = math.sin(math.radians(d))

print(a,b)

# # 入力の受け取り
# A,B=map(int,input().split())

# # mathからsqrtをインポート
# from math import sqrt

# # 計算
# x=A/sqrt(A**2+B**2)
# y=B/sqrt(A**2+B**2)

# # 答えの出力
# print(x,y)