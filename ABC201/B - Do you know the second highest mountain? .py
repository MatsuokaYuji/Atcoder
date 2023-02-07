



N = int(input())

a = []

for i in range(N):
    s,t = input().split()
    t = int(t)
    a.append([t,s])
a.sort()

print(a[-2][1])