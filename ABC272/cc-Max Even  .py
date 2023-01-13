

N = int(input())


A = list(map(int, input().split()))

A.sort(reverse=True)
m = -1
b = []
c = []

for i in A:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
# if len(b)>=2 and len(c)>=2:
#     bmax = b[0] +b[1]
#     cmax = c[0] +c[1]
#     m = max(bmax,cmax)
# elif 0<=len(b)<2 and len(c)>=2:
#     m = c[0] +c[1]
# elif 0<=len(c)<2 and len(b)>=2:
#     m = b[0] +b[1]
# else:
#     m = -1
if len(b)>=2:
    m = max(m,b[0]+b[1])
if len(c)>=2:
    m = max(m,c[0]+c[1])


if m ==-1:
    print(-1)
else:
    print(m)