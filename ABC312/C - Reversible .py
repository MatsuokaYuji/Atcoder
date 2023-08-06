









N = int(input())
S = [input() for _ in range(N)]


z =set()
for i in range(N):
    a = S[i]
    b = a[::-1]
    if a and b not in z:
        z.add(a)
# print(z)
print(len(z))