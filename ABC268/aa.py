







import collections

A,B,C,D,E = map(int,input().split())



l = []
l.append(A)
l.append(B)
l.append(C)
l.append(D)
l.append(E)

c = collections.Counter(l)
print(len(c))
# Counter({'a': 4, 'c': 2, 'b': 1})
