


N,X = map(int,input().split())
S = input()

T = ["!"]

for s in S:
    if s == "U" and T[-1] in "LR":
        T.pop()
    else:
        T.append(s)


for i in T[1:]:
    if i == "U":
        X = X//2
    if i =="L":
        X = X * 2
    if i == "R":
        X = X* 2 + 1
print(X)