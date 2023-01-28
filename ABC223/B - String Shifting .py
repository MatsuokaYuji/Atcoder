









S = input()

p = []

l = len(S)

a = S
for i in range(l):
    tmp = a[0]
    b = a[1:] + tmp
    p.append(b)
    a = b
p.sort()
print(p[0])
print(p[-1])

