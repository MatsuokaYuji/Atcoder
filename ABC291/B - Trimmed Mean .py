

N = int(input())
A = list(map(int, input().split()))




A.sort()

ans = 0

d = A[N:4*N]
# print(d)
ans = sum(d)
ans = ans/(3*N)
print(ans)