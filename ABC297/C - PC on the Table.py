




h,w = map(int,input().split())


S = [list(input()) for _ in range(h)]

# print(S)

ans = 0
for i in range(h):
    for j in range(w-1):
        if S[i][j] =="T" and S[i][j+1]=="T":
            S[i][j] ="P"
            S[i][j+1]="C"

for i in S:
    print("".join(i))
