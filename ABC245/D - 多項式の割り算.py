

import numpy



N,M = map(int,input().split())


A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]
# A.reverse()
# C.reverse()
a = numpy.poly1d(A)
c = numpy.poly1d(C)
b = c/a

print(*map(int,reversed(b[0].c)))

