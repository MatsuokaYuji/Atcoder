S = [input() for _ in range(10)]



flag = False


for i in range(10):
    for j in range(10):
        if S[i][j] == "#":
            a = i
            c = j
            flag = True
            break
    if flag:
        break

for i in range(c,10):
    if S[a][i] == ".":
        d =i-1
        break
    d =9
for i in range(a,10):
    if "#" not in S[i]:
        b = i-1
        break
    b = 9

print(a+1,b+1)
print(c+1,d+1)
