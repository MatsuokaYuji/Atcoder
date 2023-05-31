



N,M,H,K = map(int,input().split())
S = input()
z = set()

for i in range(M):
    x,y = map(int,input().split())
    z.add((x,y))

sx = 0
sy = 0

for i in range(len(S)):
    d = S[i]
    H-=1
    if d=="R":
        sx+=1
    if d=="U":
        sy+=1
    if d=="D":
        sy-=1
    if d=="L":
        sx-=1
    if H<0:
        print("No")
        exit()
    if H<K:
        if (sx,sy) in z:
            H=K
            z.remove((sx,sy))
print("Yes")
    