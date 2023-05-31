






N,M = map(int,input().split())
z =set()

for i in range(1,N+1):
    for j in range(1,N+1):
        if i!=j:
            z.add((i,j))

s = set()


for i in range(M):
    A = list(map(int, input().split()))
    for i in range(N-1):
        a = A[i]
        b = A[i+1]
        s.add((a,b))
        s.add((b,a))
ans = z-s
# print(ans)
print(len(ans)//2)
