


N = int(input())
A = list(map(int, input().split()))

B = set(i for i in range(1,N+1))
s = set()



for i in range(N):
    x = A[i]
    if (i+1) not in s:
        s.add(x)
# print(s)
ans = B-s
print(len(ans))
print(*ans)