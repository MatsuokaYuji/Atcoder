
# def factorial_for(num):
#     val = 1
#     for i in range(num, 1, -1):
#         val *= i
#     return val

N = int(input())


A = list(map(int, input().split()))

s = sum(A)
ans = 0

for i in range(N):
    tmp = A[i]**2
    tmp2 = tmp * (N-1)
    ans+=  tmp2

for i in range(N-1):
    s = s-A[i]
    tmp = A[i] * s
    ans = ans - 2*(tmp)
print(ans)