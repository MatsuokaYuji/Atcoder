
別解
# H, W = map(int, input().split())
# S = [list(input()) for _ in range(H)]
# T = [list(input()) for _ in range(H)]

# S = sorted(list(zip(*S)))
# T = sorted(list(zip(*T)))

# if S == T:
#     print('Yes')
# else:
#     print('No') 


import numpy as np
H,W=[int(hw) for hw in input().split()]
S1=[]
for _ in range(H):
    s=list(input())
    S1.append(s)

# ndarryに変換して転置を行う
S1=np.array(S1)
S1=S1.T
S1=S1.tolist()
S1=sorted(S1)

# print(S1)

t =[]

for i in range(H):
    s = list(input())
    t.append(s)
t = np.array(t)
t = t.T
t = t.tolist()
t = sorted(t)
# print(t)

for i in range(W):
    if S1[i] != t[i]:
        print("No")
        exit()
print("Yes")