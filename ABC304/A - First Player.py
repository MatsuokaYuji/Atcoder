


N = int(input())

s = []

for i in range(N):
    a,b = input().split()
    b = int(b)
    s.append((b,a))
# print(s)
# print(sorted(s))

m = sorted(s)[0][1]
# print(m)

ans = []
t = 0
for i in range(N):
    if s[i][1] == m:
        t = i
# print(t)
for i in range(N):
    d = (t+i)%N
    print(s[d][1])
