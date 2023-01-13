










A,B,C,D,E,F,X = map(int,input().split())

x1 = A+C
x2 = D+F
tDist = 0
aDist = 0
for i in range(1,X+1):
    y1 = i%x1
    if 0<y1<=A:
        tDist +=B
    elif A<y1<=x1 or y1 == 0:
        continue

for i in range(1,X+1):
    y2 = i%x2
    if 0<y2<=D:
        aDist +=E
    elif D<y2<=x2 or y2 == 0:
        continue
# print(aDist)
# print(tDist)

if aDist<tDist:
    print("Takahashi")
elif aDist>tDist:
    print("Aoki")
else:
    print("Draw")








