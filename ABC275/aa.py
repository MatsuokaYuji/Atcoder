

n = int(input())


A = list(map(int, input().split()))

ans = 1

tmp = A[0]
for i in range(n):
    if A[i] > tmp:
        tmp = A[i]
        ans = i+1

print(ans)
