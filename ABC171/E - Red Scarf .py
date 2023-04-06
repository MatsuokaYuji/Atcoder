









N = int(input())
A = list(map(int, input().split()))



s = 0

for i in range(N):
    x = A[i]
    s^=x
print(s)

ans = []

for i in range(N):
    d = s^A[i]
    ans.append(d)
print(*ans)