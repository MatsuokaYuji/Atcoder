



def check(x):
    if x==l:
        return -1
    else:
        return x



N = int(input())


S = str(N)
s = list(S)
l = len(s)
tmp = 0

cond = [-1] *(l+1)
for i in range(l):
    x = s[i]
    x = int(x)
    tmp+=x
    if x%3==0:
        cond[i] = 0
    if x%3==1:
        cond[i] = 1
    if x%3==2:
        cond[i] = 2
# print(tmp)
# print(cond)
from collections import Counter
C=Counter(cond)
# print(C)
if tmp%3==0:
    print(0)
    exit()
elif tmp%3==1:
    if C[1]>=1:
        print(check(1))
        exit()
    if C[2]>=2:
        print(check(2))
        exit()
    print(-1)
    exit()
elif tmp%3==2:
    if C[2]>=1:
        print(check(1))
        exit()
    if C[1]>=2:
        print(check(2))
        exit()
    print(-1)
    exit()
print(-1)




    