









r,c = map(int,input().split())


S = [list(input()) for _ in range(r)]

L =[]
for i in range(r):
    for j in range(c):
        if S[i][j] == "." or S[i][j] == "#":
            continue
        else:

            x = int(S[i][j])
            # print(i,j)
            for k in range(r):
                for l in range(c):
                    kyori = abs(i-k) + abs(j-l)
                    if kyori<=x and (S[k][l] == "." or S[k][l] == "#"):
                        S[k][l] ="."
            S[i][j] = "."
for i in S:
    print("".join(i))
        