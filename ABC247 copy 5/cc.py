

N = int(input())

s = [1]

for i in range(1,N):
    s = s + [i+1] + s
print(*s)