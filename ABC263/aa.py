









A,B,C,D,E = map(int,input().split())

import collections
s =[]
s.append(A)
s.append(B)
s.append(C)
s.append(D)
s.append(E)

c = collections.Counter(s)
a = c.most_common()[0][1]
b = c.most_common()[1][1]

if len(c)==2 and a ==3 and b==2:
    print("Yes")
else:
    print("No")