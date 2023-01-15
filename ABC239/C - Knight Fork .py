




def dist(a,b,c,d):
    return (a-c)**2 + (b-d)**2



x1,y1,x2,y2 = map(int,input().split())


for i in range(x1-5,x1+5):
    for j in range(y1-5,y1+5):
        if dist(i,j,x1,y1) == dist(i,j,x2,y2) == 5:
            print("Yes")
            exit()
print("No")