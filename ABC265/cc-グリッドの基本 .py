








h,w = map(int,input().split())

G = [input() for _ in range(h)]
# 無限に同じ =　一度通った箇所を通る場合

T  = [[False]* (w) for i in range(h)]
# print(T[0][0])
# print(G[0][0])
# U, D, L, R 
i = 0
j = 0
while True:
    if T[i][j] == True:
        print(-1)
        exit()
    if G[i][j] =="U":
        if i-1<0:
            print(i+1,j+1)
            exit()
        T[i][j] = True
        i -=1
    if G[i][j] =="D":
        if i>=h:
            print(i+1,j+1)
            exit()
        T[i][j] = True
        i +=1
    if G[i][j] =="L":
        if j-1<0:
            print(i+1,j+1)
            exit()
        T[i][j] = True
        j -=1
    if G[i][j] =="R":
        if j>=w:
            print(i+1,j+1)
            exit()
        T[i][j] = True
        j +=1
        

