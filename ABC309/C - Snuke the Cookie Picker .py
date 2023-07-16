
def checkAround(h,w):
    counta = 0
    if h>0:
        if S[h-1][w]  == "#":
            counta+=1
    
    if h<H-1 :
        if S[h+1][w]  == "#":
            counta+=1
    
    if w>0 :
        if S[h][w-1]  == "#" :
            counta+=1
    
    if w<W-1 :
        if S[h][w+1]  == "#" :
            counta+=1
    
    if counta >=2: 
        ans.append((h+1,w+1))
        # print(h,w)
        return True
    return False
    

H,W = map(int,input().split())


S = [input() for _ in range(H)]


ans = []
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            if checkAround(i,j):
                print(*ans[0])
                exit()