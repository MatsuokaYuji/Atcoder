

N,x,y = map(int,input().split())
A = list(map(int, input().split()))


Aodd = []
Aeven = []

for i in range(N):
    if i%2==0:
        Aodd.append(A[i])
    else:
        Aeven.append(A[i])

X = set()
Y = set()

Y.add(0)
X.add(Aodd[0])
Aodd.pop(0)
for odd in Aodd:
    tmpset = set()
    for i in X:
        tmp1 = i+odd
        tmp2 = i-odd
        tmpset.add(tmp1)
        tmpset.add(tmp2)
    X = tmpset

for even in Aeven:
    tmpset = set()
    for i in Y:
        tmp1 = i+even
        tmp2 = i-even
        tmpset.add(tmp1)
        tmpset.add(tmp2)
    Y = tmpset
if x in X and y in Y:
    print("Yes")
else:
    print("No")