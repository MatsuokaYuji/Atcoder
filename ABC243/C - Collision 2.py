





N = int(input())

p =[]

y_set = set()

for i in range(N):
    X,Y = map(int,input().split())
    p.append([X,Y])
    y_set.add(Y)

S = input()

from collections import defaultdict
dL = defaultdict(list)
dR = defaultdict(list)

for i in range(N):
    x,y = p[i]
    if S[i] == "L":
        dL[y].append(x)
    if S[i] == "R":
        dR[y].append(x)
for y in y_set:
    if 1<=len(dL[y]) and 1<=len(dR[y]):
        if min(dR[y])<max(dL[y]):
            print("Yes")
            exit()
print("No")