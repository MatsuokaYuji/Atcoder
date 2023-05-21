


def checkAround(h,w,s,x,y):
    if h>0 and w>0 and ((x==-1 and y==-1) or x==0 and y==0):
        if S[h-1][w-1]  == s:
            return [h-1,w-1,True,-1,-1]
    if h<H-1 and w<W-1 and ((x==1 and y==1) or x==0 and y==0):
        if S[h+1][w+1]  == s:
            return [h+1,w+1,True,1,1]
    if h<H-1 and w>0 and ((x==1 and y==-1) or x==0 and y==0):
        if S[h+1][w-1]  == s:
            return [h+1,w-1,True,1,-1]
    if h>0 and w<W-1 and ((x==-1 and y==1) or x==0 and y==0):
        if S[h-1][w+1]  == s:
            return [h-1,w+1,True,-1,1]
    if h>0 and ((x==-1 and y==0) or x==0 and y==0):
        if S[h-1][w]  == s:
            return [h-1,w,True,-1,0]
    if h<H-1 and ((x==1 and y==0) or x==0 and y==0):
        if S[h+1][w]  == s:
            return [h+1,w,True,1,0]
    if w>0 and ((x==0 and y==-1) or x==0 and y==0):
        if S[h][w-1]  == s:
            return [h,w-1,True,0,-1]
    if w<W-1 and ((x==0 and y==1) or x==0 and y==0):
        if S[h][w+1]  == s:
            return [h,w+1,True,0,1]
    return [h,w,False,0,0]
    



H,W = map(int,input().split())
S = [input() for _ in range(H)]

dirx = [-1,0,1]
diry = [-1,0,1]


for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            for u in dirx:
                for v in diry:
                    # print("s",i,j)
                    a,b,g,x,y = checkAround(i,j,"n",u,v)
                    
                    if g ==True:
                        # print("n",a,b)
                        a1,b1,g,x,y = checkAround(a,b,"u",x,y)
                        # print("u",a1,b1)
                    if g ==True:
                        a2,b2,g,x,y = checkAround(a1,b1,"k",x,y)
                        # print("k",a2,b2)
                    if g ==True:
                        a3,b3,g,x,y = checkAround(a2,b2,"e",x,y)
                        
                        # print("e",a3,b3)
                    if g ==True:
                        # print("e")
                        print(i+1,j+1)
                        print(a+1,b+1)
                        print(a1+1,b1+1)
                        print(a2+1,b2+1)
                        print(a3+1,b3+1)
                        exit()
                    
