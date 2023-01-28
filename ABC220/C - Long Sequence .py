





N = int(input())
A = list(map(int, input().split()))
X = int(input())

a = sum(A)

ans = 0
d = X//a
X = X-d*a
c = 0
tmp = 0
for i in range(len(A)):
    c+=A[i]
    if c>X:
        tmp = i+1
        break

ans = d*len(A)+tmp
print(ans)