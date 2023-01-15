






import numpy as np

h,w = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(h)]

transpose = []
for i in range(len(matrix[0])):
    tmp = []
    for v in matrix:
        tmp.append(v[i])
    transpose.append(tmp)
 
for i in transpose:
    print(*i)