








N = int(input())
A = list(map(int, input().split()))

ans = 1

s = set()
for i in range(N):
    s.add(A[i])
if 0 in s:
    print(0)
    exit()


for i in range(N):
    ans = ans * A[i]
    if ans>10**18:
        print(-1)
        exit()
print(ans)