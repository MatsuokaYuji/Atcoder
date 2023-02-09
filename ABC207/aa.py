






A,B,C = map(int,input().split())

a = []
a.append(A)
a.append(B)
a.append(C)
a.sort()
print(a[-1] + a[-2])