



X = int(input())


x = str(X)
s = list(x)
l = len(s)

for i in range(l):
    s[i] = int(s[i])

d = [0] * (l)
d[0] = s[0]

for i in range(1,l):
    d[i] = d[i-1] + s[i]

for i in range(l-1,0,-1):
    # 繰り上がり
    d[i-1] += d[i] // 10
    # 一桁目を採用
    d[i] = str(d[i])[-1]
d[0] = str(d[0])

print("".join(d))
    